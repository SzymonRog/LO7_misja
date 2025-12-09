from crack_password import crack_password
from passwordHelper import check_pass


def test():
    try:
        password = crack_password()
        if check_pass(password):
            print("Hasło zaakceptowano"
                  f"Hasło to: {password}")
            return True
        print("To chyba złe hasło")
        return False
    except:
        print("Coś poszło nie tak")
        return False

test()
