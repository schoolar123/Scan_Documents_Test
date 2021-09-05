import pytesseract
import cv2 as cv
import re
import os

from multilingual_pdf2text.pdf2text import PDF2Text
from multilingual_pdf2text.models.document_model.document import Document
from scanning import preprocess_image, thresholding


def pdf_ocr(file_name):
    """
    This function turns a pdf file to text. For this to work you need Tesseract and Poppler on your PC and on the
    environment path.
    :param file_name:
    :return: a list of pages of that pdf, each element is a dictionary where 'text' is key for the text
    """
    pdf_doc = Document(document_path=file_name, language='heb')
    pdf_text = PDF2Text(document=pdf_doc)
    content = pdf_text.extract()
    return content


def image_ocr(file_name):
    """
    This function reads the text from an image. For this to work you need Tesseract on your PC and on the
    environment path.
    :param file_name:
    :return:
    """
    image = cv.imread(file_name)
    clean_image = thresholding(image)
    text = pytesseract.image_to_string(clean_image, lang='heb')
    return text


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


if __name__ == '__main__':
    for image_name in os.listdir("input_images"):
        text_outputs(image_name)
