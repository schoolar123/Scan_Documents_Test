# _*_ coding: utf-8 _*_
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from ocr import image_ocr
import os


def is_divorce(text):
    return False


def is_bank_OSH(text):
    return False


def is_credit_card(text):
    return False


def is_passed_away(text):
    return False


def is_marriage(text):
    s = "תעודת נישואין"
    return s in text


def is_car_reges(text):
    return False


def is_rent_agree(text):
    return False


def is_BL_not_work(text):
    return False


def is_study_confirm(text):
    return False


def is_bank_balance(text):
    return False


def is_id_card(text):
    return False


def is_student_card(text):
    return False


class GUI:
    DOCUMENT_TYPES = ("Divorce", "Bank OSH", "Credit Card", "Passed Away",
                      "Marriage", "Car Reges", "Rent Agree", "BL Not Work",
                      "Study Confirm", "Bank Balance", "ID Card", "Student Card")
    DOCUMENT_FUNCS = [is_divorce, is_bank_OSH, is_credit_card, is_passed_away,
                      is_marriage, is_car_reges, is_rent_agree, is_BL_not_work,
                      is_study_confirm, is_bank_balance, is_id_card, is_student_card]
    NUM_OF_DOCS = len(DOCUMENT_TYPES)
    HEIGHT = (NUM_OF_DOCS + 1) * 45 + 15

    def __init__(self):
        self.gui = tk.Tk()

        self.gui.geometry(f'380x{GUI.HEIGHT}')
        self.gui.config(bg="white")

        main_frame = tk.Frame(self.gui, width=400, height=60, relief='raised', background="blue")
        main_frame.pack()

        label1 = tk.Label(main_frame, text="File Kind", width=15, bg="white")
        label1.pack(side=tk.LEFT, pady=10)
        label2 = tk.Label(main_frame, text="Result", width=15, bg="white")
        label2.pack(side=tk.RIGHT, pady=10)

        button_explore = tk.Label(main_frame, text="Browse Files Button", width=30, bg="white")
        button_explore.pack(pady=10)
        self.labels = []
        self.init_labels()

        self.gui.mainloop()

    def browse_files(self, index):
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select a File")
        file_text = image_ocr(file_name)
        result = str(GUI.DOCUMENT_FUNCS[index](file_text))
        tk.messagebox.showinfo(message=f"It is {result}!")
        self.labels[index].config(text=result)

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
                                       command=lambda x=i: self.browse_files(x), width=30,
                                       bg="white")
            button_explore.pack(pady=10)


if __name__ == '__main__':
    gui = GUI()
