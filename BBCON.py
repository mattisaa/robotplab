from arbitrator import Arbitrator
from ultrasonic import *

class BBCON:

    def __init__(self, arbitrator):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.arbitarator = Arbitrator()  # Arbitrator() objekt
        self.current_timestep = 0
        self.inactive_behaviors = list(set(self.behaviors) - set(self.active_behaviors))  # oppdateres i metoder?
        self.agent = None  # /robot, roboten den kontrollerer

    def add_behavoir(self, behavior):
        self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        self.sensobs.append(sensob)

    def activate_behavior(self, behaviour):
        if behaviour in self.behaviors:
            self.active_behaviors.append(behaviour)

    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)

    def wait(self):
        self.current_timestep += 0.5
        # pause,  allow the motor settings to remain active for a short periodof time, e.g., one half second

    def run_one_timestep(self):
        for sensob in self.sensobs:
            sensob.sensob_update()
        for behavior in self.behaviors:
            behavior.update()
        action = self.arbitarator.choose_action()
        for motob in self.motobs:
            motob.motob_update(action)   #Hva skal inn som argument?
            for motor in motob.motors:
                motor.persist(0.5)
        self.wait()  #??
        for sensob in self.sensobs:
            sensob.sensob_reset()

    def get_active_behaviors(self):
        return self.active_behaviors
