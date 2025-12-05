from update_actions import update_actions
import database

def test():
    try:
        pass1 = "11010010100100111000"
        data = database.GetDatabase(pass1)
        update_actions(data)
        if(data.GetAI(pass1).IsDeactivated()):
            return True
        else:
            return False
    except:
        print("Coś poszło nie tak!")
        return False

test()