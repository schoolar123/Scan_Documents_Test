# _*_ coding: utf-8 _*_

import re
import pytesseract
from inspect import getmembers, isfunction
from pdf2image import convert_from_path
from editing_funcs import Editing
from scanning import *

DOCUMENT_FUNCS_DICT = {
    "candidate_id": [(Editing.f005, 'heb+eng'), (Editing.f006, 'heb+eng'), (Editing.f005, 'heb'), (Editing.f006, 'heb'),
                     (Editing.f004, 'heb+eng')],
    "father_id": [(Editing.f005, 'heb+eng'), (Editing.f006, 'heb+eng'), (Editing.f005, 'heb'), (Editing.f006, 'heb'),
                  (Editing.f004, 'heb+eng')],
    "mother_id": [(Editing.f005, 'heb+eng'), (Editing.f006, 'heb+eng'), (Editing.f005, 'heb'), (Editing.f006, 'heb'),
                  (Editing.f004, 'heb+eng')],
    "candidate_current_account": [(Editing.f004, 'heb'), (Editing.f005, 'heb'), (Editing.f006, 'heb'),
                                  (Editing.f008, 'heb'), (Editing.f013, 'heb')],
    "father_current_account": [(Editing.f004, 'heb'), (Editing.f005, 'heb'), (Editing.f006, 'heb'),
                               (Editing.f008, 'heb'), (Editing.f013, 'heb')],
    "mother_current_account": [(Editing.f004, 'heb'), (Editing.f005, 'heb'), (Editing.f006, 'heb'),
                               (Editing.f008, 'heb'), (Editing.f013, 'heb')],
    "partner_current_account": [(Editing.f004, 'heb'), (Editing.f005, 'heb'), (Editing.f006, 'heb'),
                                (Editing.f008, 'heb'), (Editing.f013, 'heb')],
    "candidate_details_of_credit_charges": [(Editing.f002, 'heb'), (Editing.f013, 'heb'), (Editing.f014, 'heb'),
                                            (Editing.f015, 'heb'), (Editing.f009, 'heb')],
    "father_details_of_credit_charges": [(Editing.f002, 'heb'), (Editing.f013, 'heb'), (Editing.f014, 'heb'),
                                         (Editing.f015, 'heb'), (Editing.f009, 'heb')],
    "mother_details_of_credit_charges": [(Editing.f002, 'heb'), (Editing.f013, 'heb'), (Editing.f014, 'heb'),
                                         (Editing.f015, 'heb'), (Editing.f009, 'heb')],
    "partner_details_of_credit_charges": [(Editing.f002, 'heb'), (Editing.f013, 'heb'), (Editing.f014, 'heb'),
                                          (Editing.f015, 'heb'), (Editing.f009, 'heb')],
    "candidate_balance_concentration": [(Editing.f003, 'heb+eng'), (Editing.f004, 'heb+eng'), (Editing.f005, 'heb+eng'),
                                        (Editing.f006, 'heb+eng'), (Editing.f000, 'heb+eng')],
    "father_balance_concentration": [(Editing.f003, 'heb+eng'), (Editing.f004, 'heb+eng'), (Editing.f005, 'heb+eng'),
                                     (Editing.f006, 'heb+eng'), (Editing.f000, 'heb+eng')],
    "mother_balance_concentration": [(Editing.f003, 'heb+eng'), (Editing.f004, 'heb+eng'), (Editing.f005, 'heb+eng'),
                                     (Editing.f006, 'heb+eng'), (Editing.f000, 'heb+eng')],
    "partner_balance_concentration": [(Editing.f003, 'heb+eng'), (Editing.f004, 'heb+eng'), (Editing.f005, 'heb+eng'),
                                      (Editing.f006, 'heb+eng'), (Editing.f000, 'heb+eng')],
    "candidate_vehicle_licence": [(Editing.f006, 'heb+eng'), (Editing.f005, 'heb+eng'), (Editing.f004, 'heb+eng'),
                                  (Editing.f000, 'heb+eng'), (Editing.f003, 'heb+eng')],
    "father_vehicle_licence": [(Editing.f006, 'heb+eng'), (Editing.f005, 'heb+eng'), (Editing.f004, 'heb+eng'),
                               (Editing.f000, 'heb+eng'), (Editing.f003, 'heb+eng')],
    "mother_vehicle_licence": [(Editing.f006, 'heb+eng'), (Editing.f005, 'heb+eng'), (Editing.f004, 'heb+eng'),
                               (Editing.f000, 'heb+eng'), (Editing.f003, 'heb+eng')],
    "partner_vehicle_licence": [(Editing.f006, 'heb+eng'), (Editing.f005, 'heb+eng'), (Editing.f004, 'heb+eng'),
                                (Editing.f000, 'heb+eng'), (Editing.f003, 'heb+eng')],
    "father_rental_agreement": [(Editing.f003, 'heb'), (Editing.f002, 'heb'), (Editing.f013, 'heb'),
                                (Editing.f017, 'heb'), (Editing.f008, 'heb')],
    "candidate_rental_agreement": [(Editing.f003, 'heb'), (Editing.f002, 'heb'), (Editing.f013, 'heb'),
                                   (Editing.f017, 'heb'), (Editing.f008, 'heb')],
    "mother_rental_agreement": [(Editing.f003, 'heb'), (Editing.f002, 'heb'), (Editing.f013, 'heb'),
                                (Editing.f017, 'heb'), (Editing.f008, 'heb')],
    "partner_rental_agreement": [(Editing.f003, 'heb'), (Editing.f002, 'heb'), (Editing.f013, 'heb'),
                                 (Editing.f017, 'heb'), (Editing.f008, 'heb')],
    "marriage_certificate": [(Editing.f006, 'heb+eng'), (Editing.f005, 'heb+eng'), (Editing.f004, 'heb+eng'),
                             (Editing.f013, 'heb+eng'), (Editing.f000, 'heb+eng')],
    "divorce_certificate": [(Editing.f005, 'heb'), (Editing.f006, 'heb'), (Editing.f013, 'heb'), (Editing.f019, 'heb'),
                            (Editing.f014, 'heb+eng')],
    "candidate_pay_stubs": [(Editing.f008, 'heb+eng'), (Editing.f013, 'heb'), (Editing.f006, 'heb+eng'),
                            (Editing.f005, 'heb'), (Editing.f014, 'heb')],
    "father_pay_stubs": [(Editing.f008, 'heb+eng'), (Editing.f013, 'heb'), (Editing.f006, 'heb+eng'),
                         (Editing.f005, 'heb'), (Editing.f014, 'heb')],
    "mother_pay_stubs": [(Editing.f008, 'heb+eng'), (Editing.f013, 'heb'), (Editing.f006, 'heb+eng'),
                         (Editing.f005, 'heb'), (Editing.f014, 'heb')],
    "partner_pay_stubs": [(Editing.f008, 'heb+eng'), (Editing.f013, 'heb'), (Editing.f006, 'heb+eng'),
                          (Editing.f005, 'heb'), (Editing.f014, 'heb')],
    "student_certificate": [(Editing.f006, 'heb+eng'), (Editing.f005, 'heb+eng'), (Editing.f004, 'heb+eng'),
                            (Editing.f000, 'heb'), (Editing.f019, 'heb+eng')],
    "partner_death_certificate": [(Editing.f006, 'heb+eng'), (Editing.f005, 'heb+eng'), (Editing.f004, 'heb+eng'),
                                  (Editing.f000, 'heb+eng'), (Editing.f014, 'heb+eng')],
    "father_death_certificate": [(Editing.f006, 'heb+eng'), (Editing.f005, 'heb+eng'), (Editing.f004, 'heb+eng'),
                                 (Editing.f000, 'heb'), (Editing.f014, 'heb+eng')],
    "mother_death_certificate": [(Editing.f006, 'heb+eng'), (Editing.f005, 'heb+eng'), (Editing.f004, 'heb+eng'),
                                 (Editing.f000, 'heb'), (Editing.f014, 'heb+eng')],
    "candidate_no_work": [(Editing.f012, 'heb+eng'), (Editing.f013, 'heb'), (Editing.f006, 'heb+eng'),
                          (Editing.f004, 'heb'), (Editing.f013, 'heb')],
    "partner_no_work": [(Editing.f012, 'heb+eng'), (Editing.f013, 'heb'), (Editing.f006, 'heb+eng'),
                        (Editing.f004, 'heb'), (Editing.f013, 'heb')],
    "father_no_work": [(Editing.f012, 'heb+eng'), (Editing.f013, 'heb'), (Editing.f006, 'heb+eng'),
                       (Editing.f004, 'heb'), (Editing.f013, 'heb')],
    "mother_no_work": [(Editing.f012, 'heb+eng'), (Editing.f013, 'heb'), (Editing.f006, 'heb+eng'),
                       (Editing.f004, 'heb'), (Editing.f013, 'heb')],
    "study_confirmation": [(Editing.f003, 'heb+eng'), (Editing.f017, 'heb+eng'), (Editing.f019, 'heb+eng'),
                           (Editing.f013, 'heb+eng'), (Editing.f005, 'heb+eng')],
    "father_cpa_approval_on_income": None, "mother_cpa_approval_on_income": None,
    "partner_cpa_approval_on_income": None, "exception_expenses": None,
    "approve_allowance_amount": None, "results_sheet": None, "cv": None,
    "warrior_certificate": None, "discharge_certificate": None,
    "monthly_budget_from_kibbutz": None, "providing_assistance_from_kibbutz": None,
    "candidate_mortgage": None, "father_mortgage": None,
    "mother_mortgage": None, "partner_mortgage": None,
    "tuition": None, "candidate_mole_report": None, "partner_mole_report": None,
    "father_mole_report": None, "mother_mole_report": None
    }


def ocr(file_name, file_kind=None):
    """
    This function is the main OCR function which extracts text from a file (pdf or image).
    :param file_kind:
    :param file_name:
    :return: a generator for the text of the file (each iteration it returns text).
    """
    if file_kind is None:
        funcs = None
    else:
        funcs = DOCUMENT_FUNCS_DICT[file_kind]
    if file_name.endswith("pdf"):
        return pdf_ocr(file_name, funcs)
    return image_ocr(file_name, funcs)


def pdf_ocr(file_name, funcs):
    """
    This function turns a pdf file to text. For this to work you need Tesseract and Poppler on your PC and on the
    environment path.
    :param funcs:
    :param file_name:
    :return: a generator for the pages of the file (each iteration it returns text).
    """
    content = convert_from_path(file_name)
    for page in content:
        yield image_extractor(np.array(page), funcs)


def image_ocr(file_name, funcs):
    """
    This function reads the text from an image. For this to work you need Tesseract on your PC and on the
    environment path.
    :param funcs:
    :param file_name:
    :return: a generator for the image (each iteration it returns text).
    """
    img = cv.imread(file_name)
    yield image_extractor(img, funcs)


def image_extractor(img, funcs):
    """
    This function go all over the editing funcs (in a generator), extract the text from the image and cleans it a bit.
    :param funcs:
    :param img:
    :return: a generator for the text of the image (each iteration it returns text).
    """
    if funcs is None:
        funcs = [f[1] for f in getmembers(Editing, isfunction)]
        for func in funcs:
            heb_txt = pytesseract.image_to_string(func(img), lang='heb')
            heb_eng_txt = pytesseract.image_to_string(func(img), lang='heb+eng')
            cleaned_heb_txt = re.sub(r"\s\s+", "\n", heb_txt).strip()
            cleaned_heb_eng_txt = re.sub(r"\s\s+", "\n", heb_eng_txt).strip()
            yield cleaned_heb_txt, cleaned_heb_eng_txt
    else:
        for func, lang in funcs:
            txt = pytesseract.image_to_string(func(img), lang=lang)
            cleaned_txt = re.sub(r"\s\s+", "\n", txt).strip()
            yield [cleaned_txt]
