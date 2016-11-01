

class Behavior:

    def __init__(self, bbcon):
        self.bbcon = bbcon
        self.sensobs = []
        self.motor_recommendations = []  # one rec per motob, all motobs are used by all behaviors
        self.active_flag = False  # True = active, False = inactive
        self.halt_request = False  # ??
        self.priority = None
        self.match_degree = 0
        self.weight = self.priority * self.match_degree   # Base for selecting the winning behavior


    def consider_deactivation(self):
        if self.active_flag:
            # Test om den burde være inactive, if set active_flag til False

    def consider_activation(self):
        if not self.active_flag:
            # Sjekk om burde være active, if set active_flag til True

    def update_behavior(self):
        self.consider_activation()
        self.consider_deactivation()
        matchdeg = self.sense_and_act()
        self.weight = self.priority * matchdeg

    def sense_and_act(self):

        return match_degree