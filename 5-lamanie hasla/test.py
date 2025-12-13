from crack_password import crack_password
from passwordHelper import check_pass


def test():
    komunikat = ""
    try:
        password = crack_password()
        if check_pass(password):
            komunikat += f"Hasło zaakceptowano\nHasło to: {password}"
            print(komunikat)
            return True

        komunikat +="Odmowa dostępu nieprawidłowe hasło"
        print(komunikat)
        return False
    except:
        komunikat += "Coś poszło nie tak"
        print(komunikat)
        return False

test()
