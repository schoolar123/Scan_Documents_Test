# _*_ coding: utf-8 _*_


def not_exists(text):
    return False


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
    key1 = "ריכוז יתרות"
    key2 = "ריכוז היתרות"
    for page in text:
        for output in page:
            if key1 in output or key2 in output:
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
