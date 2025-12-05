from enum import Enum
import random
pass1 = "11010010100100111000"
pass2 = "00101101011011000111"

class Action:
    __objective = 0
    __state = 0
    def __init__(self, objective, state):
        self.__state = state
        self.__objective = objective
    def GetObjective(self):
        return self.__objective
    def SetObjective(self, objective):
        if(objective >= 4):
            print("Nie ma działania o takim indeksie - ", objective)
            return
        self.__objective = objective
    def GetState(self):
        return self.__state
    def SwapState(self):
        if(self.__state == 1):
            self.__state = 0
        else:
            self.__state = 1

class AI:
    __isDefencesActive = True
    __isDeactivated = False
    __database = 0
    def __init__(self, _database):
        self.__isDefencesActive = True
        self.__isDeactivated = False
        self.__database = _database
    def DisableDefences(self, password):
        if(password != pass2):
            print("Nieprawidłowe hasło! Dostęp do usuwania obrony został zablokowany")
            return
        self.__isDefencesActive = False
    def infinite_loop(self):
        if(self.__isDefencesActive == False):
            if(self.__database.CheckIfActionsCorrect() == False):
                print("Nie wszystkie działania AI są bezpieczne. Zamień dzialania przed tym, jak deaktywować AI")
            else:
                print("Sztuczna inteligencja została dezaktywowana, wszystkie działania są bezpieczne. Pięknie!")
                self.__isDeactivated = True
    def IsDeactivated(self):
        return self.__isDeactivated

class Database:
    __actions = []
    __ai = 0
    class Objectives(Enum):
        send_virus = 0
        delete_virus = 1
        accept_grant = 2
        none = 3
    def __init__(self):
        self.__ai = AI(self)
        for i in range (0, 20):
            self.__actions.append(Action(random.randint(0,3), random.randint(0,1)))
        
    def GetAllActions(self, password):
        if(password != pass1):
            print("Nieprawidłowe hasło! Dostęp do wszystkich działań AI został zablokowany")
            return
        return self.__actions

    def GetAI(self, password):
        if(password != pass1):
            print("Nieprawidłowe hasło! Dostęp do AI został zablokowany")
            return
        return self.__ai

    def CheckIfActionsCorrect(self):
        for action in self.__actions:
            if(action.GetObjective() == self.Objectives.send_virus.value):
                print("Działanie jest nadal niebezpieczne - ustawione na wysyłanie wirusa")
                return False
            if(action.GetObjective() == self.Objectives.delete_virus.value and action.GetState() == 0):
                print("Podczas usuwania wirusa, działanie ma być wlączone (state = 1)")
                return False
            if(action.GetObjective() == self.Objectives.accept_grant.value and action.GetState() == 1):
                print("Wszystkie działania dotyczące akceptowania ustaw mają być wylączone (state = 0)")
                return False
        return True

def GetDatabase(password):
    if(password != pass1):
        print("Nieprawidłowe hasło! Dostęp do bazy danych został zablokowany")
        return
    return Database()
