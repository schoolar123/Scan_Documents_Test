import numpy as np
import cv2 as cv
import imutils

from perspective import four_point_transform

from skimage.filters import threshold_local

BOX_OFFSET = 0
WHITE = 255
BLACK = 0

# Cosmetics
GREEN = (0, 255, 0)
RED = (0, 0, 255)
MEDIUM_LINE_LENGTH = 2

# Hyper parameters
EDGE_KERNEL_SIZE = 3
PERI_PERCENTAGE = 0.001
TRANSFORM_KERNEL_SIZE = 13
THRESHOLD_KERNEL_SIZE = TRANSFORM_KERNEL_SIZE - 4
THRESHOLD_BIAS = 4
CANNY_T1 = 25
CANNY_T2 = 220


def find_edges(image_name):
    """
    This function is for finding the edges in the image
    :param image_name:
    :return:
    """
    image = cv.imread(f"input_images\\{image_name}")
    try:
        ratio = image.shape[0] / 500.0
    except:
        t = 1
    orig = image.copy()
    image = imutils.resize(image, height=500)

    # Changing the image to a BLACK & WHITE image
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Blurring the image to eliminate noises in the image
    gray_image = cv.GaussianBlur(gray_image, (EDGE_KERNEL_SIZE, EDGE_KERNEL_SIZE), 0)

    # med = np.median(gray_image)
    # lower = int(max(0, 0.7* med))
    # upper = int(min(255, 1.3*med))
    # print(lower, upper)

    # Using the Canny edge detection algorithm (with the gradient of the image),
    # Intensity of an edge is the norm of (Gradient_x, Gradient_y).
    # Any edge that has higher intensity than T2 is considered an edge.
    # Any edge that has lower intensity than T2 (but higher than T1) and is connected to a considered edge, is also
    # considered as an edge.
    # Any other edge is not considered as an edge.
    # L2gradient if TRUE,  using the norm 2 to calculate the intensity: sqrt of (Gradient_x**2 + Gradient_y**2).
    #            if FALSE, using the norm 1 to calculate the intensity: |Gradient_x| + |Gradient_y**2|.
    # apertureSize is the sobel kernel size (which is for smoothing the image in one direction and deriving the image
    # on the perpendicular direction.
    edged = cv.Canny(gray_image, CANNY_T1, CANNY_T2, L2gradient=True, apertureSize=3)
    cv.imwrite(f"output_images\\edged_{image_name}", edged)
    # cv.imshow("Image", image)
    # cv.imshow("Gray Image", gray_image)
    # cv.imshow("Edged", edged)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    return edged.copy(), image.copy(), orig, ratio


def old_find_contour(edged, image):
    cnts = cv.findContours(edged, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv.contourArea, reverse=True)[:5]
    screenCnt = None

    for c in cnts:

        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.02 * peri, True)

        # finding an edge with 4 corners
        if len(approx) == 4:
            screenCnt = approx
            break

    # cv.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
    # cv.imshow("Outline", image)
    # cv.waitKey(0)
    # cv.destroyAllWindows()


def arc_length(contour):
    '''
    Calculating the length of a closed contour
    :param contour:
    :return:
    '''
    return cv.arcLength(contour, True)


def contour_arc(contour):
    arc = cv.arcLength(contour, True)
    # contour = list(contour.reshape(-1, 2))
    # min_x = min(contour, key=lambda x: x[0])[0]
    # max_x = max(contour, key=lambda x: x[0])[0]
    # diff_x = max_x - min_x
    #
    # min_y = min(contour, key=lambda x: x[1])[1]
    # max_y = max(contour, key=lambda x: x[1])[1]
    # diff_y = max_y - min_y
    #
    # return diff_y * diff_x + 100*diff_y
    return arc


def find_contour(edged, image, image_name):
    """
    :param edged: The edged image
    :param image:
    :return:
    """

    # Finding all the contours in the edged image.
    cnts = cv.findContours(edged, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # Sorting the closed contours by their lengths (maybe taking the max is enough).
    cnts = sorted(cnts, key=contour_arc, reverse=True)

    # Calculating the closed contour length (which is the perimeter of the object).
    peri = cv.arcLength(cnts[0], True)

    # Approximating the the object contour (polynomial curve).
    # The 2nd parameter is approximation accuracy, the closer it gets to 0 the tighter it fits the contour.
    screen_contour = cv.approxPolyDP(cnts[0], PERI_PERCENTAGE * peri, True)

    # Drawing the contour around the object
    cv.drawContours(image, [screen_contour], -1, GREEN, MEDIUM_LINE_LENGTH)

    # Finding the rotated rectangle that surrounds the object in order to know the angle for the the rotation.
    rect = cv.minAreaRect(screen_contour)
    box = cv.boxPoints(rect)
    box = np.int0(box)

    # Adding an offset to the box in order to catch a bit more than the object
    box += np.array(
        [[-BOX_OFFSET, -BOX_OFFSET], [BOX_OFFSET, -BOX_OFFSET], [BOX_OFFSET, BOX_OFFSET], [-BOX_OFFSET, BOX_OFFSET]])

    # Drawing the rotated rectangle
    # cv.drawContours(image, [box], -1, RED, MEDIUM_LINE_LENGTH)
    # cv.imwrite(f"output_images\\{image_name}_boxed.jpg", image)
    # cv.imshow("Boxed", image)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    return box


def perspective_transform(org_image, screen_contour, ratio):
    """
    This function is taking the object out of the image and rotating it.
    :param org_image: the original image
    :param screen_contour: the contour of the object in the image
    :param ratio: the ratio between the original and the processed image
    :return: the final scanned image
    """
    # Transforming the object from the image (which is rotating the object to be straight and discarding
    # the rest of the image).
    warped = four_point_transform(org_image, screen_contour.reshape(4, 2) * ratio)
    return warped


def thresholding(image):
    """
    This function turns the image to a clear white with black lines.
    :param image:
    :return:
    """
    # Changing the image to a BLACK & WHITE image
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # cv.imshow("warped1", warped)
    # cv.waitKey(0)

    # Blurring the image to eliminate noises in the image (maybe not needed).
    # threshold_image = cv.GaussianBlur(gray_image, (TRANSFORM_KERNEL_SIZE, TRANSFORM_KERNEL_SIZE), 0)
    # cv.imshow("warped2", threshold_image)
    # cv.waitKey(0)

    # Thresholding the object using an adaptive gaussian threshold in order to eliminate noise and bold the data,
    # changing the image to white with black lines.
    threshold_image = cv.adaptiveThreshold(gray_image, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                           THRESHOLD_KERNEL_SIZE,
                                           THRESHOLD_BIAS)

    # T = threshold_local(gray_image, 11, offset=10, method="gaussian")
    # threshold_image = (gray_image > T).astype(np.uint8) * 255

    # ret3, threshold_image = cv.threshold(threshold_image, BLACK, WHITE, cv.THRESH_BINARY + cv.THRESH_OTSU)
    return threshold_image


def preprocess_image(image_name):
    edged_image, resized_image, org_image, ratio = find_edges(image_name)
    screen_contour = find_contour(edged_image, resized_image, image_name)
    warped = perspective_transform(org_image, screen_contour, ratio)
    scanned_image = thresholding(warped)
    cv.imwrite(f"output_images\\{image_name[:-4]}_scanned{image_name[-4:]}", scanned_image)
    return scanned_image
