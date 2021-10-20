# _*_ coding: utf-8 _*_


def is_doc_recon(text, doc_kind):
    for page in text:
        for output in page:
            if doc_kind(output):
                return True
    return False


def not_exists(text):
    return False


def is_divorce(text):
    key = "תעודת גרושין"
    if key in text[0]:
        return True
    new_output = text[0]
    for word1 in teudat_words():
        new_output = new_output.replace(word1, "תעודת")
    for word2 in gerushin_words():
        new_output = new_output.replace(word2, "גרושין")
    return key in new_output


def is_bank_OSH(text):
    key = "יתרה בחשבון"
    return key in text[0]


def is_credit_card(text):
    key = "מסטרקארד"
    return key in text[0]


def is_passed_away(text):
    key = "תעודת פטירה"
    if key in text[0]:
        return True
    new_output = text[0]
    for word1 in teudat_words():
        new_output = new_output.replace(word1, "תעודת")
    for word2 in ptira_words():
        new_output = new_output.replace(word2, "פטירה")
    return key in new_output


def is_marriage(text):
    key = "תעודת נישואין"
    if key in text[0]:
        return True
    new_output = text[0]
    for word1 in teudat_words():
        new_output = new_output.replace(word1, "תעודת")
    for word2 in nisuin_words():
        new_output = new_output.replace(word2, "נישואין")
    return key in new_output


def is_car_reges(text):
    key = "רישיון רכב"
    return key in text[0]


def is_rent_agree(text):
    key = "חוזה שכירות"
    return key in text[0]


def is_BL_not_work(text):
    key = "מעמד לא עובד"
    if key in text[0]:
        return True
    new_output = text[0]
    for word1 in oved_words():
        new_output = new_output.replace(word1, "עובד")
    return key in new_output


def is_study_confirm(text):
    key = "אישור לימודים"
    return key in text[0]


def is_bank_balance(text):
    key1 = "ריכוז יתרות"
    key2 = "ריכוז היתרות"
    return key1 in text[0] or key2 in text[0]


def is_id_card(text):
    key = "תעודת זהות"
    if key in text[0]:
        return True
    new_output = text[0]
    for word1 in teudat_words():
        new_output = new_output.replace(word1, "תעודת")
    return key in new_output


def is_student_card(text):
    key1 = "כרטיס סטודנט"
    key2 = "תעודת סטודנט"
    if key1 in text[0] or key2 in text[0]:
        return True
    new_output = text[0]
    for word1 in teudat_words():
        new_output = new_output.replace(word1, "תעודת")
    for word2 in student_words():
        new_output = new_output.replace(word2, "סטודנט")
    for word3 in cartis_words():
        new_output = new_output.replace(word3, "כרטיס")
    return key1 in new_output or key2 in new_output


def is_paycheck(text):
    key = "ניכויים"
    if key in text[0]:
        return True
    new_output = text[0]
    for word1 in nikuim_words():
        new_output = new_output.replace(word1, "ניכויים")
    return key in new_output


def teudat_words():
    return ["תקודת", "תעורת", "תענדת", "העודת", "תפודת", "תעורה", "תקורת"]


def gerushin_words():
    return ["נרושיך", "נרוטין", "גרושיך", "נרושין", "גרוטין", "גדושין"]


def hamosad_words():
    return ["המזסד"]


def lebituah_words():
    return ["לביטות"]


def medinat_words():
    return ["מדיגת", "מדונת", "מרינת"]


def nisuin_words():
    return ["גישואין", "נשואין", "נשואיץ", "נשואיך", "נסואיך", "בשואין"]


def oved_words():
    return ["עובר"]


def tlush_words():
    return ["חלוש", "תלוס"]


def sachar_words():
    return ["טכר"]


def nikuim_words():
    return ["נוכויים", "ניבויים", "גיכויים"]


def ptira_words():
    return ["פטירת"]


def israel_words():
    return ["יטראל"]


def cartis_words():
    return ["כרטים", "ברטים", "ברטיס"]


def student_words():
    return ["סטורנט"]


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
                 "study_confirmation": is_study_confirm,
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
