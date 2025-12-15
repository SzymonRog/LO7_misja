from find_commit import find_log
from datetime import datetime

def find_commit(id):
    with open('commits.txt', "r") as f:
        for commit in f:
            data = commit.strip().split("|")
            if data[0] == id:
                return commit

def test():
    komunikat = ""
    try:
        commit_data = 'gg23f42 | 2025-12-04 03:45:22 | Final optimization | Borda.cpp |main | [AutoTask] CorpTech'
        branch = 'main'
        file = 'Borda.cpp'

        date = datetime.strptime("2025-12-04 10:00:00", "%Y-%m-%d %H:%M:%S")
        answer = 'gg23f42'
        user_answer = find_log(date, branch, file)

        if user_answer == answer:
            komunikat += "Brawo udało ci sie!\n"
            komunikat += f"Ostatni commit przed awarią: \n{commit_data}\nCoś tu smierdzi czyżby ktoś tu specjanlnie próbował sabotowac nasz system?\n'AutoTask - CorpTech'  co to ma wogóle znaczyć?"
            print(komunikat)
            return True
        else:
            user_commit = find_commit(user_answer).strip().split("|")
            komunikat += "Coś jest chyba nie tak.\n"
            komunikat += f"Ten commit chyba jest w porządku: \n{user_commit[0]} | {user_commit[1]} | {user_commit[2]} | {user_commit[3]} | {user_commit[4]} | {user_commit[5]}"
            print(komunikat)
            return False
    except:
        komunikat += "Nie ma takiego commita."
        print(komunikat)
        return False

test()


