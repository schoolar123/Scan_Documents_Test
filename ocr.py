# _*_ coding: utf-8 _*_

import re
import pytesseract
from inspect import getmembers, isfunction
from pdf2image import convert_from_path
from editing_funcs import Editing
from scanning import *


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
    funcs = [f[1] for f in getmembers(Editing, isfunction)]
    for func in funcs:
        txt = pytesseract.image_to_string(func(img), lang='heb')
        cleaned_txt = re.sub(r"\s\s+", "\n", txt).strip()
        yield cleaned_txt
