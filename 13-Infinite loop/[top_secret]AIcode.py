'''
from enum import Enum

class Action:
    def GetObjective(self):
        return self.objective

    def SetObjective(self, objective):
        self.objective = objective

    def GetState(self):
        return self.__state

    def SwapState(self):
        if(self.state == 1):
            self.state = 0
        else:
            self.state = 1

class AI:
    isDefencesActive = True
    isDeactivated = False

    def DisableDefences(self, password):
        if(password != password):
            return Exceptions.ShutDown
        self.isDefencesActive = False

    def infinite_loop(self):
        if(self.isDefencesActive == True):
            return None
        a = 0
        while(true):
            a += 1

class Database:
    class Objectives(Enum):
        send_virus
        delete_virus
        accept_grant
        none
        
    def GetAllActions(self, password):
        if(password != pass1):
            return Exceptions.ShutDown
        return self.actions

    def GetAI(self, password):
        if(password != pass1):
            return Exceptions.ShutDown
        return self.ai

'''
