from ocr import *
import skimage.transform
import pandas as pd
import matplotlib.pyplot as plt
from analyzing import DOCUMENT_DICT


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


def print_output(file_generator):
    """
    This function prints the output of the editing funcs.
    :param file_generator: The generator that generates the different outputs.
    :return:
    """
    for page in file_generator:
        for i, out in enumerate(page):
            print(f"function {i}:")
            print("Only Hebrew:", out[0])
            print("With English:", out[1])
            print("************************************")


def analyze_doc_scores(text, row):
    """
    This function analyzes all the different editing funcs and gives them a score based of the parameters from the
    excel file.
    :param text: The generator that generates the different outputs.
    :param row: The specific row from the excel file that contains the score parameters of a document file.
    :return: The scores of the different outputs (1 for only heb results and 1 for heb+eng results)
    """
    num_of_funcs = len(getmembers(Editing, isfunction))
    scores_1, scores_2 = np.zeros(num_of_funcs, int), np.zeros(num_of_funcs, int)
    lengths_1, lengths_2 = np.zeros(num_of_funcs, int), np.zeros(num_of_funcs, int)
    doc_kind = row[0]
    for page in text:
        for i, output in enumerate(page):
            scores_1[i] += analyze_helper(doc_kind, output[0], row)
            scores_2[i] += analyze_helper(doc_kind, output[1], row)
            lengths_1[i] += len(output[0])
            lengths_2[i] += len(output[1])
    scores_1[np.argmax(lengths_1)] += 10
    scores_2[np.argmax(lengths_2)] += 10
    # scores_1 is the array for only heb results and scores_2 is the array for heb+eng results
    return scores_1, scores_2


def analyze_helper(doc_kind, txt, row):
    """
    This function is a helper for the analyze_doc_scores function, which sums the score of a specific output.
    :param doc_kind: The kind of the document.
    :param txt: The text of the specific output.
    :param row: The row in the excel file that contains the score parameters for this document.
    :return: The score of a specific output.
    """
    score = DOCUMENT_DICT[doc_kind]([txt])
    for i in range(1, len(row), 2):
        if not pd.isnull(row[i]) and str(row[i]) in txt:
            score += int(row[i + 1])
    return score


def plot_results(results, file_name):
    """
    This function plot the results of all the scores of the different outputs.
    :param results: a pair of arrays of the results, the first is the heb results and the second is the heb+eng results.
    :param file_name: The name of the specific file (which the results are of this file).
    :return:
    """
    labels = [str(num) for num in range(len(results[0]))]
    x = np.arange(len(labels))  # the label locations
    width = 0.25  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, results[0], width, label="heb")
    rects2 = ax.bar(x + width / 2, results[1], width, label="heb+eng")
    ax.set_ylabel("Scores")
    ax.set_xlabel("Functions")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.bar_label(rects1, padding=2)
    ax.bar_label(rects2, padding=2)
    plt.title(f"Results of {file_name}")
    fig.tight_layout()
    plt.savefig(f"results_graph/{file_name[13:-4]}_results.png")
    print(f"{file_name[13:-4]}_results.png saved!")


def analyze_docs():
    """
    This function go all over the docs in the excel file, analyzes the scores of the different outputs and
    plot the results with a bar plot.
    No need to change this function (only add new docs in the excel file).
    :return:
    """
    df = pd.read_excel(io="documents_data.xlsx")
    num_of_docs = len(df)
    for row_num in range(num_of_docs):
        row = df.iloc[row_num]
        file_name = row[0]
        txt_gen = ocr(file_name)
        results = analyze_doc_scores(txt_gen, row[1:])
        plot_results(results, file_name)


def output_image(image_file_name):
    txt_gen = ocr(image_file_name)
    print_output(txt_gen)


if __name__ == '__main__':
    analyze_docs()
