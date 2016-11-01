
from BBCON import BBCON
from random import uniform

class Arbitrator():

    def __init__(self):
        self.behaviors = None

    def choose_action(self, method=None):
        self.behaviors = BBCON.get_active_behaviors()
        if method == 0:
           return self.stochastic(self.behaviors)
        else:
           return self.deterministic(self.behaviors)

    def stochastic(self, behaviors):
        choiseList = []
        bot = 0
        for i in range(len(behaviors)):
            choiseList.append((bot, behaviors[i].get_value))
            bot = behaviors[i].get_value
        choise = uniform(0, max(behaviors.get_value))
        for i in range(len(choiseList)):
            if choiseList[i][0] <= choise < choiseList[i][1]:
                return choiseList[i]

    def deterministic(self, behaviors):
        return max(behaviors.get_value)
