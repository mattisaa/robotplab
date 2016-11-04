
from BBCON import BBCON
from random import uniform

class Arbitrator():

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
