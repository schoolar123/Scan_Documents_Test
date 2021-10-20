# _*_ coding: utf-8 _*_
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from ocr import *
from analyzing import *
import os


class GUI:
    DOCUMENT_TYPES = ["divorce_certificate", "candidate_current_account", "candidate_details_of_credit_charges",
                      "father_death_certificate",
                      "marriage_certificate", "candidate_vehicle_licence", "candidate_rental_agreement",
                      "candidate_no_work",
                      "candidate_study_confirmation", "candidate_balance_concentration", "candidate_id",
                      "student_certificate", "candidate_pay_stubs"]
    # txt = ocr(file_name)
    # result = DOCUMENT_DICT[document_type](txt)
    NUM_OF_DOCS = len(DOCUMENT_TYPES)
    HEIGHT = (NUM_OF_DOCS + 1) * 45 + 15

    def __init__(self):
        self.gui = tk.Tk()
        self.gui.geometry(f'680x{GUI.HEIGHT}')
        self.gui.config(bg="white")
        self.init_main_frame()
        self.labels = []
        self.init_labels()
        self.gui.mainloop()

    def init_main_frame(self):
        """
        This function initializes the main frame of the GUI.
        :return:
        """
        main_frame = tk.Frame(self.gui, width=780, height=60, relief='raised', background="blue")
        main_frame.pack()
        label1 = tk.Label(main_frame, text="File Kind", width=15, bg="white")
        label1.pack(side=tk.LEFT, pady=5)
        label2 = tk.Label(main_frame, text="Result", width=15, bg="white")
        label2.pack(side=tk.RIGHT, pady=5)
        button_explore = tk.Label(main_frame, text="Browse Files Button", width=60, bg="white")
        button_explore.pack(pady=5)

    def init_labels(self):
        """
        This function initializes the labels of the GUI (the buttons, the names of files' kind and the result).
        :return:
        """
        for i, doc_name in enumerate(GUI.DOCUMENT_TYPES):
            main_frame = tk.Frame(self.gui, width=700, height=60, relief='raised', bg="white")
            main_frame.pack()
            label1 = tk.Label(main_frame, text=doc_name, width=30, bg="white")
            label1.pack(side=tk.LEFT, pady=10)
            label2 = tk.Label(main_frame, text="empty", width=25, bg="white")
            label2.pack(side=tk.RIGHT, pady=10)
            self.labels.append(label2)
            button_explore = tk.Button(main_frame, text=f"Browse {doc_name} Files",
                                       command=lambda x=i: self.browse_files(x), width=40, bg="white")
            button_explore.pack(pady=10)

    def browse_files(self, index):
        """
        This function:
        1. Lets the user choose a file (image or pdf) from his computer.
        2. Extracts the text from the file (as a generator).
        3. Analyzes the text and stores True (in the result variable) if the image is really what was asked for
           or False otherwise.
        4. Alerts the user whether the result is True or False.
        5. Stores the result in label of the file that was asked for in the GUI.
        :param index: The index of the file kind according to the order of the list DOCUMENT_TYPES.
        :return:
        """
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select a File")
        if file_name:
            file_text = ocr(file_name)
            # This variable (document_type) should be a parameter in the function from the Front End
            document_type = GUI.DOCUMENT_TYPES[index]
            result = is_doc_recon(file_text, DOCUMENT_DICT[document_type])
            tk.messagebox.showinfo(message=f"{GUI.DOCUMENT_TYPES[index]} is {result}!")
            self.labels[index].config(text=result)


if __name__ == '__main__':
    gui = GUI()
