import pytesseract
import cv2 as cv


from multilingual_pdf2text.pdf2text import PDF2Text
from multilingual_pdf2text.models.document_model.document import Document
from scanning import perspective_transform


def pdf_ocr(file_name):
    pdf_doc = Document(document_path=file_name, language='heb')
    pdf_text = PDF2Text(document=pdf_doc)
    content = pdf_text.extract()
    return content


def image_ocr(file_name):
    image = cv.imread(file_name)
    clean_image = perspective_transform(image)
    text = pytesseract.image_to_string(clean_image, lang='heb')
    return text


if __name__ == '__main__':
    FILE_NAME = "input_images/marriage.jpg"
    print(image_ocr(FILE_NAME))
