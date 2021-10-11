# _*_ coding: utf-8 _*_
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from ocr import *
import os


def is_divorce(text):
    for page in text:
        for output in page:
            if "תעודת גרושין" in output:
                return True
            new_output = output
            for word1 in teudat_words():
                new_output = new_output.replace(word1, "תעודת")
            for word2 in gerushin_words():
                new_output = new_output.replace(word2, "גרושין")
            if "תעודת גרושין" in new_output:
                return True
    return False


def is_bank_OSH(text):
    for page in text:
        for output in page:
            if 'יתרה בחשבון' in output:
                return True
    return False


def is_credit_card(text):
    for page in text:
        for output in page:
            if "מסטרקארד" in output:
                return True
    return False


def is_passed_away(text):
    for page in text:
        for output in page:
            if "תעודת פטירה" in output:
                return True
            new_output = output
            for word1 in teudat_words():
                new_output = new_output.replace(word1, "תעודת")
            for word2 in ptira_words():
                new_output = new_output.replace(word2, "פטירה")
            if "תעודת פטירה" in new_output:
                return True
    return False


def is_marriage(text):
    key = "תעודת נישואין"
    for page in text:
        for output in page:
            if key in output:
                return True
            new_output = output
            for word1 in teudat_words():
                new_output = new_output.replace(word1, "תעודת")
            for word2 in nisuin_words():
                new_output = new_output.replace(word2, "נישואין")
            if key in new_output:
                return True
    return False


def is_car_reges(text):
    key = "רישיון רכב"
    for page in text:
        for output in page:
            if key in output:
                return True
    return False


def is_rent_agree(text):
    key = "חוזה שכירות"
    for page in text:
        for output in page:
            if key in output:
                return True
    return False


def is_BL_not_work(text):
    key = "מעמד לא עובד"
    for page in text:
        for output in page:
            if key in output:
                return True
            new_output = output
            for word1 in oved_words():
                new_output = new_output.replace(word1, "עובד")
            if key in new_output:
                return True
    return False


def is_study_confirm(text):
    key = "אישור לימודים"
    for page in text:
        for output in page:
            if key in output:
                return True
    return False


def is_bank_balance(text):
    key = "ריכוז יתרות"
    for page in text:
        for output in page:
            if key in output:
                return True
    return False


def is_id_card(text):
    key = "תעודת זהות"
    for page in text:
        for output in page:
            if key in output:
                return True
            new_output = output
            for word1 in teudat_words():
                new_output = new_output.replace(word1, "תעודת")
            if key in new_output:
                return True
    return False


def is_student_card(text):
    key1 = "כרטיס סטודנט"
    key2 = "תעודת סטודנט"
    for page in text:
        for output in page:
            if key1 in output or key2 in output:
                return True
            new_output = output
            for word1 in teudat_words():
                new_output = new_output.replace(word1, "תעודת")
            for word2 in student_words():
                new_output = new_output.replace(word2, "סטודנט")
            for word3 in cartis_words():
                new_output = new_output.replace(word3, "כרטיס")
            if key1 in new_output or key2 in new_output:
                return True
    return False


def is_paycheck(text):
    key = "ניכויים"
    for page in text:
        for output in page:
            if key in output:
                return True
            new_output = output
            for word1 in nikuim_words():
                new_output = new_output.replace(word1, "ניכויים")
            if key in new_output:
                return True
    return False


class GUI:
    DOCUMENT_TYPES = ("Divorce", "Bank OSH", "Credit Card", "Passed Away",
                      "Marriage", "Car Reges", "Rent Agree", "BL Not Work",
                      "Study Confirm", "Bank Balance", "ID Card", "Student Card", "Paycheck")
    DOCUMENT_FUNCS = [is_divorce, is_bank_OSH, is_credit_card, is_passed_away,
                      is_marriage, is_car_reges, is_rent_agree, is_BL_not_work,
                      is_study_confirm, is_bank_balance, is_id_card, is_student_card, is_paycheck]
    NUM_OF_DOCS = len(DOCUMENT_TYPES)
    HEIGHT = (NUM_OF_DOCS + 1) * 45 + 15

    def __init__(self):
        self.gui = tk.Tk()
        self.gui.geometry(f'380x{GUI.HEIGHT}')
        self.gui.config(bg="white")
        self.init_main_frame()
        self.labels = []
        self.init_labels()
        self.gui.mainloop()

    def init_main_frame(self):
        main_frame = tk.Frame(self.gui, width=400, height=60, relief='raised', background="blue")
        main_frame.pack()
        label1 = tk.Label(main_frame, text="File Kind", width=15, bg="white")
        label1.pack(side=tk.LEFT, pady=10)
        label2 = tk.Label(main_frame, text="Result", width=15, bg="white")
        label2.pack(side=tk.RIGHT, pady=10)
        button_explore = tk.Label(main_frame, text="Browse Files Button", width=30, bg="white")
        button_explore.pack(pady=10)

    def init_labels(self):
        for i, doc_name in enumerate(GUI.DOCUMENT_TYPES):
            main_frame = tk.Frame(self.gui, width=400, height=60, relief='raised', bg="white")
            main_frame.pack()
            label1 = tk.Label(main_frame, text=doc_name, width=15, bg="white")
            label1.pack(side=tk.LEFT, pady=10)
            label2 = tk.Label(main_frame, text="empty", width=15, bg="white")
            label2.pack(side=tk.RIGHT, pady=10)
            self.labels.append(label2)
            button_explore = tk.Button(main_frame, text=f"Browse {doc_name} Files",
                                       command=lambda x=i: self.browse_files(x), width=30, bg="white")
            button_explore.pack(pady=10)

    def browse_files(self, index):
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select a File")
        file_text = ocr(file_name)
        result = str(GUI.DOCUMENT_FUNCS[index](file_text))
        tk.messagebox.showinfo(message=f"{GUI.DOCUMENT_TYPES[index]} is {result}!")
        self.labels[index].config(text=result)


if __name__ == '__main__':
    # gui = GUI()
    t = ocr("input_images\id.jpg")
    for k in t:
        for d in k:
            print(d)
