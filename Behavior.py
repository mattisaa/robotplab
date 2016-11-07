


class Behavior:

    def __init__(self, bbcon,priority):
        self.bbcon = bbcon
        self.sensobs = None
        self.motor_recommendations = []  # one rec per motob, all motobs are used by all behaviors
        self.active_flag = True  # True = active, False = inactive
        self.halt_request = False  # ??
        self.priority = priority
        self.match_degree = 0
        self.weight = self.priority * self.match_degree   # Base for selecting the winning behavior


    def consider_deactivation(self):

        # Test om den burde være inactive, if set active_flag til False
        return False

    def consider_activation(self):

        # Sjekk om burde være active, if set active_flag til True
        return True

    def update_behavior(self):
        self.consider_activation()
        self.consider_deactivation()
        matchdeg = self.sense_and_act()
        self.weight = self.priority * matchdeg

    def sense_and_act(self):

        raise NotImplementedError


