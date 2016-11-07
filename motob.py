
from motors import Motors

class Motob():

    def __init__(self, motors=Motors(), value=[]):
        self.motors = motors
        self.value = value

    def update(self, motor_rec):
        self.value.append(motor_rec)
        self.operationalize(motor_rec)

    def operationalize(self, motor_rec):
        #Her må vi finne verdier som funker vha. testing
        dur = motor_rec[1] * (1/120)
        if motor_rec[0] == 'L':
            self.motors.left(0.5, dur)
        elif motor_rec[0] == 'R':
            self.motors.right(0.5, dur)
        elif motor_rec[0] == 'F':
            self.motors.forward(0.5, dur)
        elif motor_rec[0] == 'B':
            self.motors.backward(0.5, dur)
            self.motors.left(0.5, 0.5)

    def motorStop(self):
        self.motors.stop()
