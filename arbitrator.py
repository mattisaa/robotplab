
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

    def __init__(self, bbcon=BBCON()):
        self.bbcon = bbcon
        self.motor_recs = None
        self.halt_req = None

    def choose_action(self, stoc=False):
        behaviors = self.bbcon.active_behaviors()
        if stoc is True:
            self.stochastic(behaviors)
        elif stoc is False:
            self.deterministic(behaviors)
        if self.motor_recs.halt_req is True:
            self.halt_req = True
        return self.motor_recs, self.halt_req

    def stochastic(self, behaviors):
        total_weight = 0
        for behavior in behaviors:
            total_weight += behavior.weight
        randnum = uniform(0, total_weight)
        i = 0
        for behavior in behaviors:
            if i <= randnum < behavior.weight:
                self.motor_recs = behavior
                break
            i = behavior.weight

    def deterministic(self, behaviors):
        largest_weight = -1
        for behavior in behaviors:
            if behavior.weight > largest_weight:
                largest_weight = behavior.weight
                self.motor_recs = behavior

