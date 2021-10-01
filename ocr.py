# _*_ coding: utf-8 _*_
import numpy as np
import skimage.transform
from pdf2image import convert_from_path
from scanning import *


def teudat_words():
    return ["תקודת", "תעורת", "תענדת", "העודת", "תפודת", "תעורה", "תקורת"]


def gerushin_words():
    return ["נרושיך", "נרוטין", "גרושיך", "נרושין", "גרוטין", "גדושין"]


def hamosad_words():
    return ["המזסד"]


def lebituah_words():
    return ["לביטות"]


def medinat_words():
    return ["מדיגת", "מדונת", "מרינת"]


def nisuin_words():
    return ["גישואין", "נשואין", "נשואיץ", "נשואיך", "נסואיך", "בשואין"]


def oved_words():
    return ["עובר"]


def tlush_words():
    return ("חלוש", "תלוס")


def sachar_words():
    return ("טכר")


def nikuim_words():
    return ["נוכויים", "ניבויים", "גיכויים"]


def ptira_words():
    return ["פטירת"]


def israel_words():
    return ["יטראל"]


def cartis_words():
    return "כרטים", "ברטים", "ברטיס"


def student_words():
    return ["סטורנט"]


def ocr(file_name):
    if file_name.endswith("pdf"):
        return pdf_ocr(file_name)
    return image_ocr(file_name)


def pdf_ocr(file_name):
    """
    This function turns a pdf file to text. For this to work you need Tesseract and Poppler on your PC and on the
    environment path.
    :param file_name:
    :return: a list of pages of that pdf, each element is a dictionary where 'text' is key for the text
    """
    content = convert_from_path(file_name)
    for page in content:
        yield image_extracter(np.array(page))


def image_ocr(file_name):
    """
    This function reads the text from an image. For this to work you need Tesseract on your PC and on the
    environment path.
    :param file_name:
    :return:
    """
    img = cv.imread(file_name)
    yield image_extracter(img)


def image_extracter(img):
    for func in FUNCS:
        txt = pytesseract.image_to_string(func(img), lang='heb')
        cleaned_txt = re.sub(r"\s\s+", "\n", txt).strip()
        yield cleaned_txt



def text_outputs(image_name):
    scanned_image = preprocess_image(image_name)

    # Extracting the text after selecting the object
    text1 = pytesseract.image_to_string(scanned_image, lang='heb')

    # Extracting the text only after thresholding
    text2 = image_ocr(f"input_images/{image_name}")

    with open(f"output_texts/{image_name[:-4]}_output1.txt", "w") as out1:
        h = re.sub(r"\n+ *", "\n", text1)
        h2 = re.sub(r"\n+", "\n", h)
        out1.write(h2)
    with open(f"output_texts/{image_name[:-4]}_output2.txt", "w") as out2:
        c = re.sub(r"\n+ *", "\n", text2)
        c2 = re.sub(r"\n+", "\n", c)
        out2.write(c2)


def erosion_test(file_name):
    """
    This function is thickening the text.
    :param file_name:
    :return:
    """
    image = cv.imread(f"input_images/{file_name}")
    kernel_size = 3
    clean_image = thresholding(image)
    kernel2 = np.ones((kernel_size, kernel_size), np.uint8)
    kernel2[0, 0] = 0
    kernel2[0, 2] = 0
    kernel2[2, 0] = 0
    kernel2[2, 2] = 0
    eroded = cv.erode(clean_image, kernel2)
    eroded_original = cv.erode(image, kernel2)
    cv.imshow("clean image", clean_image)
    cv.imshow("Eroded", eroded)
    cv.imshow("original image", image)
    cv.imshow("eroded original", eroded_original)
    cv.waitKey(0)
    cv.destroyAllWindows()

    text1 = pytesseract.image_to_string(image, lang='heb')
    text2 = pytesseract.image_to_string(clean_image, lang='heb')
    text3 = pytesseract.image_to_string(eroded, lang='heb')
    text4 = pytesseract.image_to_string(eroded_original, lang='heb')

    with open("file1.txt", "w") as f1:
        f1.write(text1)
    with open("file2.txt", "w") as f1:
        f1.write(text2)
    with open("file3.txt", "w") as f1:
        f1.write(text3)
    with open("file4.txt", "w") as f1:
        f1.write(text4)


def dilation_test(file_name):
    """
    This function is thinning the text in the image.
    :param file_name:
    :return:
    """
    rescale_factor = 1.5
    image = cv.imread(f"input_images/{file_name}")
    # Enlarging the image by factor of 1.5
    image = np.uint8(
        skimage.transform.rescale(image, (rescale_factor, rescale_factor), multichannel=True, preserve_range=True))
    kernel_size = 3
    clean_image = thresholding(image)
    kernel2 = np.ones((kernel_size, kernel_size), np.uint8)
    kernel2[0, 0] = 0
    kernel2[0, 2] = 0
    kernel2[2, 0] = 0
    kernel2[2, 2] = 0

    dilated = cv.dilate(clean_image, kernel2)

    original_dilated = cv.dilate(image, kernel2)

    # test_txts(image, clean_image, dilated, original_dilated)
    cv.imshow("original image", image)
    cv.imshow("clean image", clean_image)
    cv.imshow("dilated", dilated)
    cv.imshow("dilated original", original_dilated)
    cv.waitKey(0)
    cv.destroyAllWindows()


def test_txts(*images):
    """
    This function extracts the text from any amount of images and writes it into text files.
    :param images:
    :return:
    """
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image, lang='heb')
        with open(f"test_file{i + 1}.txt", "w") as f:
            f.write(text)
