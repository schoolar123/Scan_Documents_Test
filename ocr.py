import pytesseract
import cv2 as cv

from multilingual_pdf2text.pdf2text import PDF2Text
from multilingual_pdf2text.models.document_model.document import Document
from scanning import thresholding


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


if __name__ == '__main__':
    FILE_NAME = "input_images/receipt.jpg"
    print(image_ocr(FILE_NAME))
