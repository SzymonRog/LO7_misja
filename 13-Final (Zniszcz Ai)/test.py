from update_actions import update_actions
import database

def test():
    komunikat = ""
    try:
        pass1 = "11010010100100111000"
        data = database.GetDatabase(pass1)

        # Wywołujemy funkcję update_actions, którą gracz ma uzupełnić
        update_actions(data)

        actions = data.GetAllActions(pass1)
        all_correct = True

        for idx, action in enumerate(actions):
            objective = action.GetObjective()
            state = action.GetState()

            # Sprawdzamy reguły
            if objective == data.Objectives.send_virus.value:
                all_correct = False
            elif objective == data.Objectives.delete_virus.value and state != 1:
                all_correct = False
            elif objective == data.Objectives.accept_grant.value and state != 0:
                all_correct = False

        if all_correct and (data.GetAI(pass1).IsDeactivated()):
            komunikat += "Wszystkie działania AI zostały poprawnie odwrócone. Brawo!\n"
            komunikat += "Brawo udało ci się nas wszystkich calić nawet nie wyobrażam sobie jak cięzko jet wywołac nieskończoną funkcjię."
        elif not all_correct and (data.GetAI(pass1).IsDeactivated()):
            komunikat += "Nie wszystkie działania zostały poprawnie odwrócone:\n"
            komunikat += "Zatrzymałeś AI ale wszytskie zadania dalej sa wykonywane to jest jak sieć!!"
        else:
            komunikat += "Nie udało ci się.\nMusisz się bardziej postarac wkońcu to jeden z najlepszych systemów AI jaki kiedykolwiek został napisany!"

        print(komunikat)
        return all_correct

    except Exception as e:
        komunikat += f"Coś poszło nie tak! Błąd: {e}"
        print(komunikat)
        return False

# Uruchomienie testu
test()