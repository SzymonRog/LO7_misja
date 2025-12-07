from crack_password import crack_password
from passwordHelper import check_pass


def test():
    try:
        if check_pass(crack_password()):
            print("Hasło zaakceptowano")
            return True
        print("To chyba złe hasło")
        return False
    except:
        print("Coś poszło nie tak")
        return False
