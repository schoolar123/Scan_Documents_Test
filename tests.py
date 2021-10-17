from ocr import *
import skimage.transform
import pandas as pd
import matplotlib.pyplot as plt


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
    for page in file_generator:
        for i, out in enumerate(page):
            print(f"function {i}:")
            print(out)
            print("************************************")


def analyze_bank_balance(text, row):
    scores = []
    key1 = "ריכוז יתרות"
    key2 = "ריכוז היתרות"
    max_len = 0
    index_of_winner = 0
    for page in text:
        for k, output in enumerate(page):
            score = 0
            if key1 in output or key2 in output:
                score += 15
            for i in range(0, len(row), 2):
                if not pd.isnull(row[i]) and row[i] in output:
                    score += int(row[i + 1])
            if len(output) > max_len:
                max_len = len(output)
                index_of_winner = k
            scores.append(score)
    scores[index_of_winner] += 10
    return scores


def plot_results(results, file_name):
    labels = [str(num) for num in range(len(results))]
    x = np.arange(len(labels))  # the label locations
    width = 0.5  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, results, width)
    ax.set_ylabel("Scores")
    ax.set_xlabel("Functions")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.bar_label(rects1, padding=3)
    plt.title(f"Results of {file_name}")
    plt.show()


def analyze_docs():
    ANALYZE_DICT = {"input_images/itrot.png": analyze_bank_balance}
    NUM_OF_DOCS = len(ANALYZE_DICT)
    df = pd.read_excel(io="documents_data.xlsx")
    for row_num in range(NUM_OF_DOCS):
        row = df.iloc[row_num]
        file_name = row[0]
        txt_gen = ocr(file_name)
        results = ANALYZE_DICT[file_name](txt_gen, row[1:])
        plot_results(results, file_name)


if __name__ == '__main__':
    analyze_docs()
