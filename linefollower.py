__author__ = 'mattisaraya'


import Behavior


class Linefollower(Behavior.Behavior):

    def __init__(self,bbcon,priority):
        super.__init__(bbcon,priority)
        self.match_degree=1

    def sense_and_act(self):
        value=self.sensobs.get_value()
        