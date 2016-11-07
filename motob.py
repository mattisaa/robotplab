
from motors import Motors

class Motob():

    def __init__(self, motors=Motors(), value=[]):
        self.motors = motors
        self.value = value

<<<<<<< HEAD
    def motob_update(self, mr=None):
        if mr[0] == self.motors[0]:
            self.setMotorValue(side=0, value=mr[1])
        elif mr[1] == self.motors[1]:
            self.setMotorValue(side=1, value=mr[1])
        else:
            self.setMotorValue(value=mr[1])
        self.operationalize(self.value)
=======
    def update(self, motor_rec):
        self.value.append(motor_rec)
        self.operationalize(motor_rec)
>>>>>>> master

    def operationalize(self, motor_rec):
        dur = motor_rec[1] * (1/120)
        if motor_rec[0] == 'L':
            self.motors.left(0.5, dur) #Verdier må endres under testing
        elif motor_rec[0] == 'R':
            self.motors.right(0.5, dur) #Verdier må endres under testing
        elif motor_rec[0] == 'F':
            self.motors.forward(0.5, dur)
        elif motor_rec[0] == 'B':
            self.motors.backward(0.5, dur)
            self.motors.left(0.5, 0.5)

<<<<<<< HEAD
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

#hei
=======
    def motorStop(self):
        self.motors.stop()
>>>>>>> master
