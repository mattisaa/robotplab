from BBCON import BBCON
from sensor import CameraSensob


class Behavior:

    def __init__(self):
        self.bbcon = BBCON()
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
            # Forskjellig for hver behavior
            if ??:
                self.active_flag = False
                self.bbcon.deactivate_behavior(self)

    def consider_activation(self):
        if not self.active_flag:
            # Sjekk om burde være active, if set active_flag til True
            # Forskjellig for hver behavior
            if ??:
                self.active_flag = True
                self.bbcon.activate_behavior(self)

    def update_behavior(self):
        self.consider_activation()
        self.consider_deactivation()
        matchdeg = self.sense_and_act()
        self.weight = self.priority * matchdeg

    def sense_and_act(self):

        return match_degree


<<<<<<< HEAD
class CameraBehaviour(Behavior):

    def __init__(self):
        self.camera_sensob = CameraSensob()

    def take_picture(self):
        color_value = self.camera_sensob.dominant_color_in_picture()
        if color_value == 'red':
=======
>>>>>>> master
