import skimage.transform
from scanning import *


class Editing:

    @staticmethod
    def f000(img):
        """
        1. Changes the image to a gray image.
        :param img:
        :return:
        """
        new_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return new_img

    @staticmethod
    def f001(img):
        """
        1. Changes the image to a gray image.
        2. Thresholding the image to make it only black or white (no gray colors).
        :param img:
        :return:
        """
        new_img = Editing.f000(img)
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f002(img):
        """
        1. Changes the image to a gray image.
        2. Blurring the image a bit in order to smooth it.
        3. Thresholding the image to make it only black or white (no gray colors).
        :param img:
        :return:
        """
        kernel_size = 3
        new_img = Editing.f000(img)
        new_img = cv.GaussianBlur(new_img, (kernel_size, kernel_size), 0)
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f003(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 0.75x size.
        :param img:
        :return:
        """
        rescale_factor = 0.75
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        return new_img

    @staticmethod
    def f004(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 1.5x size.
        :param img:
        :return:
        """
        rescale_factor = 1.5
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        return new_img

    @staticmethod
    def f005(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 2x size.
        :param img:
        :return:
        """
        rescale_factor = 2.0
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        return new_img

    @staticmethod
    def f006(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 2.5x size.
        :param img:
        :return:
        """
        rescale_factor = 2.5
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        return new_img

    @staticmethod
    def f007(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 0.75x size.
        3. Thresholding the image to make it only black or white (no gray colors).
        :param img:
        :return:
        """
        rescale_factor = 0.75
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f008(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 1.5x size.
        3. Thresholding the image to make it only black or white (no gray colors).
        :param img:
        :return:
        """
        rescale_factor = 1.5
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f009(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 2x size.
        3. Thresholding the image to make it only black or white (no gray colors).
        :param img:
        :return:
        """
        rescale_factor = 2.0
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f010(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 2.5x size.
        3. Thresholding the image to make it only black or white (no gray colors).
        :param img:
        :return:
        """
        rescale_factor = 2.5
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f011(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 0.75x size.
        3. Blurring the image a bit in order to smooth it.
        4. Thresholding the image to make it only black or white (no gray colors).
        :param img: 
        :return: 
        """""
        rescale_factor = 0.75
        kernel_size = 3
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        new_img = cv.GaussianBlur(new_img, (kernel_size, kernel_size), 0)
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f012(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 1.5x size.
        3. Blurring the image a bit in order to smooth it.
        4. Thresholding the image to make it only black or white (no gray colors).
        :param img:
        :return:
        """
        rescale_factor = 1.5
        kernel_size = 3
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        new_img = cv.GaussianBlur(new_img, (kernel_size, kernel_size), 0)
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f013(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 2x size.
        3. Blurring the image a bit in order to smooth it.
        4. Thresholding the image to make it only black or white (no gray colors).
        :param img:
        :return:
        """
        rescale_factor = 2.0
        kernel_size = 3
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        new_img = cv.GaussianBlur(new_img, (kernel_size, kernel_size), 0)
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f014(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 2.5x size.
        3. Blurring the image a bit in order to smooth it.
        4. Thresholding the image to make it only black or white (no gray colors).
        :param img:
        :return:
        """
        rescale_factor = 2.5
        kernel_size = 3
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        new_img = cv.GaussianBlur(new_img, (kernel_size, kernel_size), 0)
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f015(img):
        """
        1. Changes the image to a gray image.
        2. Thresholding the image to make it only black or white (no gray colors).
        3. Dilating the image (reduces the width of the text).
        :param img:
        :return:
        """
        new_img = Editing.f001(img)
        new_img = dilation(new_img)
        return new_img

    @staticmethod
    def f016(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 0.75x size.
        3. Thresholding the image to make it only black or white (no gray colors).
        4. Dilating the image (reduces the width of the text).
        :param img:
        :return:
        """
        new_img = Editing.f007(img)
        new_img = dilation(new_img)
        return new_img

    @staticmethod
    def f017(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 1.5x size.
        3. Thresholding the image to make it only black or white (no gray colors).
        4. Dilating the image (reduces the width of the text).
        :param img:
        :return:
        """
        new_img = Editing.f008(img)
        new_img = dilation(new_img)
        return new_img

    @staticmethod
    def f018(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 2x size.
        3. Thresholding the image to make it only black or white (no gray colors).
        4. Dilating the image (reduces the width of the text).
        :param img:
        :return:
        """
        new_img = Editing.f009(img)
        new_img = dilation(new_img)
        return new_img

    @staticmethod
    def f019(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 2.5x size.
        3. Thresholding the image to make it only black or white (no gray colors).
        4. Dilating the image (reduces the width of the text).
        :param img:
        :return:
        """
        new_img = Editing.f010(img)
        new_img = dilation(new_img)
        return new_img

    @staticmethod
    def f020(img):
        """
        1. Changes the image to a gray image.
        2. Thresholding the image to make it only black or white (no gray colors).
        3. Eroding the image (increases the width of the text).
        :param img:
        :return:
        """
        new_img = Editing.f001(img)
        new_img = erosion(new_img)
        return new_img

    @staticmethod
    def f021(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 0.75x size.
        3. Thresholding the image to make it only black or white (no gray colors).
        4. Eroding the image (increases the width of the text).
        :param img:
        :return:
        """
        new_img = Editing.f007(img)
        new_img = erosion(new_img)
        return new_img

    @staticmethod
    def f022(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 1.5x size.
        3. Thresholding the image to make it only black or white (no gray colors).
        4. Eroding the image (increases the width of the text).
        :param img:
        :return:
        """
        new_img = Editing.f008(img)
        new_img = erosion(new_img)
        return new_img

    @staticmethod
    def f023(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 2x size.
        3. Thresholding the image to make it only black or white (no gray colors).
        4. Eroding the image (increases the width of the text).
        :param img:
        :return:
        """
        new_img = Editing.f009(img)
        new_img = erosion(new_img)
        return new_img

    @staticmethod
    def f024(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 2.5x size.
        3. Thresholding the image to make it only black or white (no gray colors).
        4. Eroding the image (increases the width of the text).
        :param img:
        :return:
        """
        new_img = Editing.f010(img)
        new_img = erosion(new_img)
        return new_img


    @staticmethod
    def f025(img):
        """
        1. Changes the image to a gray image.
        2. Rescaling the image to be 3x size.
        :param img:
        :return:
        """
        rescale_factor = 3
        new_img = Editing.f000(img)
        new_img = np.uint8(skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,preserve_range=True))
        return new_img