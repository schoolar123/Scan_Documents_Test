# _*_ coding: utf-8 _*_

import re
import pytesseract
from inspect import getmembers, isfunction
from pdf2image import convert_from_path
from editing_funcs import Editing
from scanning import *


def ocr(file_name):
    """
    This function is the main OCR function which extracts text from a file (pdf or image).
    :param file_name:
    :return: a generator for the text of the file (each iteration it returns text).
    """
    if file_name.endswith("pdf"):
        return pdf_ocr(file_name)
    return image_ocr(file_name)


def pdf_ocr(file_name):
    """
    This function turns a pdf file to text. For this to work you need Tesseract and Poppler on your PC and on the
    environment path.
    :param file_name:
    :return: a generator for the pages of the file (each iteration it returns text).
    """
    content = convert_from_path(file_name)
    for page in content:
        yield image_extractor(np.array(page))


def image_ocr(file_name):
    """
    This function reads the text from an image. For this to work you need Tesseract on your PC and on the
    environment path.
    :param file_name:
    :return: a generator for the image (each iteration it returns text).
    """
    img = cv.imread(file_name)
    yield image_extractor(img)


def image_extractor(img):
    """
    This function go all over the editing funcs (in a generator), extract the text from the image and cleans it a bit.
    :param img:
    :return: a generator for the text of the image (each iteration it returns text).
    """
    funcs = [f[1] for f in getmembers(Editing, isfunction)]
    for func in funcs:
        heb_txt = pytesseract.image_to_string(func(img), lang='heb')
        heb_eng_txt = pytesseract.image_to_string(func(img), lang='heb+eng')
        cleaned_heb_txt = re.sub(r"\s\s+", "\n", heb_txt).strip()
        cleaned_heb_eng_txt = re.sub(r"\s\s+", "\n", heb_eng_txt).strip()
        yield cleaned_heb_txt, cleaned_heb_eng_txt
