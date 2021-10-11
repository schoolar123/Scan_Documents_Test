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
    return ["חלוש", "תלוס"]


def sachar_words():
    return ["טכר"]


def nikuim_words():
    return ["נוכויים", "ניבויים", "גיכויים"]


def ptira_words():
    return ["פטירת"]


def israel_words():
    return ["יטראל"]


def cartis_words():
    return ["כרטים", "ברטים", "ברטיס"]


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