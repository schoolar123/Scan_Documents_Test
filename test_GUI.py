# _*_ coding: utf-8 _*_
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from ocr import *
from analyzing import *
import os


class GUI:
    DOCUMENT_TYPES = ["Divorce", "Bank OSH", "Credit Card", "Passed Away",
                      "Marriage", "Car Reges", "Rent Agree", "BL Not Work",
                      "Study Confirm", "Bank Balance", "ID Card", "Student Card", "Paycheck"]
    DOCUMENT_FUNCS = [is_divorce, is_bank_OSH, is_credit_card, is_passed_away,
                      is_marriage, is_car_reges, is_rent_agree, is_BL_not_work,
                      is_study_confirm, is_bank_balance, is_id_card, is_student_card, is_paycheck]
    DOCUMENT_DICT = {"candidate_id": is_id_card, "father_id": is_id_card, "mother_id": is_id_card,
                     "candidate_current_account": is_bank_OSH, "father_current_account": is_bank_OSH,
                     "mother_current_account": is_bank_OSH, "partner_current_account": is_bank_OSH,
                     "candidate_details_of_credit_charges": is_credit_card,
                     "father_details_of_credit_charges": is_credit_card,
                     "mother_details_of_credit_charges": is_credit_card,
                     "partner_details_of_credit_charges": is_credit_card,
                     "candidate_balance_concentration": is_bank_balance,
                     "father_balance_concentration": is_bank_balance,
                     "mother_balance_concentration": is_bank_balance, "partner_balance_concentration": is_bank_balance,
                     "candidate_vehicle_licence": is_car_reges, "father_vehicle_licence": is_car_reges,
                     "mother_vehicle_licence": is_car_reges, "father_rental_agreement": is_rent_agree,
                     "partner_vehicle_licence": is_car_reges, "candidate_rental_agreement": is_rent_agree,
                     "mother_rental_agreement": is_rent_agree, "partner_rental_agreement": is_rent_agree,
                     "marriage_certificate": is_marriage, "divorce_certificate": is_divorce,
                     "candidate_pay_stubs": is_paycheck, "father_pay_stubs": is_paycheck,
                     "mother_pay_stubs": is_paycheck, "partner_pay_stubs": is_paycheck,
                     "student_certificate": is_student_card, "partner_death_certificate": is_passed_away,
                     "father_death_certificate": is_passed_away, "mother_death_certificate": is_passed_away,
                     "candidate_no_work": is_BL_not_work, "partner_no_work": is_BL_not_work,
                     "father_no_work": is_BL_not_work, "mother_no_work": is_BL_not_work,
                     "father_cpa_approval_on_income": not_exists, "mother_cpa_approval_on_income": not_exists,
                     "partner_cpa_approval_on_income": not_exists, "exception_expenses": not_exists,
                     "approve_allowance_amount": not_exists, "results_sheet": not_exists, "cv": not_exists,
                     "warrior_certificate": not_exists, "discharge_certificate": not_exists,
                     "monthly_budget_from_kibbutz": not_exists, "providing_assistance_from_kibbutz": not_exists,
                     "candidate_mortgage": not_exists, "father_mortgage": not_exists,
                     "mother_mortgage": not_exists, "partner_mortgage": not_exists,
                     "tuition": not_exists, "candidate_mole_report": not_exists, "partner_mole_report": not_exists,
                     "father_mole_report": not_exists, "mother_mole_report": not_exists,
                     }
    # txt = ocr(file_name)
    # result = DOCUMENT_DICT[document_type](txt)
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
        """
        This function initializes the main frame of the GUI.
        :return:
        """
        main_frame = tk.Frame(self.gui, width=400, height=60, relief='raised', background="blue")
        main_frame.pack()
        label1 = tk.Label(main_frame, text="File Kind", width=15, bg="white")
        label1.pack(side=tk.LEFT, pady=10)
        label2 = tk.Label(main_frame, text="Result", width=15, bg="white")
        label2.pack(side=tk.RIGHT, pady=10)
        button_explore = tk.Label(main_frame, text="Browse Files Button", width=30, bg="white")
        button_explore.pack(pady=10)

    def init_labels(self):
        """
        This function initializes the labels of the GUI (the buttons, the names of files' kind and the result).
        :return:
        """
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
        """
        This function:
        1. Lets the user choose a file (image or pdf) from his computer.
        2. Extracts the text from the file (as a generator).
        3. Analyzes the text and stores True (in the result variable) if the image is really what was asked for
           or False otherwise.
        4. Alerts the user whether the result is True or False.
        5. Stores the result in label of the file that was asked for in the GUI.
        :param index: The index of the file kind according to the order of the list DOCUMENT_TYPES and DOCUMENT_FUNCS.
        :return:
        """
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select a File")
        if file_name:
            file_text = ocr(file_name)
            result = str(GUI.DOCUMENT_FUNCS[index](file_text))
            tk.messagebox.showinfo(message=f"{GUI.DOCUMENT_TYPES[index]} is {result}!")
            self.labels[index].config(text=result)


if __name__ == '__main__':
    gui = GUI()
