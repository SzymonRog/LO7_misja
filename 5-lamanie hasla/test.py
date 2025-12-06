from bruteForce import bruteForce
from passwordHelper import checkPass


def test():
    try:
        if checkPass(bruteForce()):
            print("Hasło zaakceptowano")
            return True
        print("To chyba złe hasło")
        return False
    except:
        print("Coś poszło nie tak")
        return False
