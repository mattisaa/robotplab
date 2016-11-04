
from motors import Motors

class Motob():

    def __init__(self):
        self.motors = []
        self.value = [0, 0]

    def motob_update(self, mr=None):
        if mr[0] == self.motors[0]:
            self.setMotorValue(side=0, value=mr[1])
        elif mr[1] == self.motors[1]:
            self.setMotorValue(side=1, value=mr[1])
        else:
            self.setMotorValue(value=mr[1])
        self.operationalize(self.value)

    def operationalize(self, value=None):
        Motors.set_value(val=value)

    def setMotorValue(self, side=None, value=None):
        # Need to convert mr-value to actualspeed of belt here
        if side == 0:
            self.value[0] = value
            self.value[1] = value
        elif side == 1:
            self.value[0] = value
            self.value[1] = value
        else:
            self.value[0] = value
            self.value[1] = self.value[0]

#yo