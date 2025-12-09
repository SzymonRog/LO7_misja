from passwordHelper import get_youth_word_2025
from passwordHelper import check_pass


def crack_password():
    words = get_youth_word_2025()
    password_1st = "D03591"
    password_2nd = "114AS51"

    for word in words:
        password = password_1st + word + password_2nd
        if check_pass(password.upper()):
            return password.upper()

    return ""


