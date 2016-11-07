__author__ = 'mattisaraya'


from PIL import Image
import time
import ultrasonic
import zumo_button
import camera
import reflectance_sensors
import irproximity_sensor
from imager2 import Imager


class Sensob():

<<<<<<< HEAD
    def update(self):
        raise NotImplementedError

    def get_value(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError



class UltrasonicSensOb(Sensob):

    def __init__(self):
        self.sensor=ultrasonic.Ultrasonic()

    def update(self):
        self.sensor.update()

    def get_value(self):
        return self.sensor.get_value()

    def reset(self):
        self.sensor.reset()

class IrProximitySensOb(Sensob):

    def __init__(self):
        self.sensor=irproximity_sensor.IRProximitySensor()

    def update(self):
        self.sensor.update()

    def get_value(self):
        return self.sensor.get_value()

    def reset(self):
        self.sensor.reset()

class ReflectanceSensOb(Sensob):


    #her brukes max og min for å kalibrere, kan evt sette auto_calibrate til TRUE for auto-kalibrering
    def __init__(self):
        self.sensor=reflectance_sensors.ReflectanceSensors(auto_calibrate=False,min_reading=100,max_reading=1000)
        self.get_value()

    def update(self):
        self.updated_value=self.sensor.update()

    def get_value(self):
        self.value=self.sensor.get_value()
        return self.value

    def reset(self):
        self.sensor.reset()

class CameraSensob(Sensob):
=======
>>>>>>> master


    def update(self):
        raise NotImplementedError

    def get_value(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError



class UltrasonicSensOb(Sensob):

    def __init__(self):
        self.sensor=ultrasonic.Ultrasonic()

    def update(self):
        self.sensor.update()

    def get_value(self):
        return self.sensor.get_value()

    def reset(self):
        self.sensor.reset()

class IrProximitySensOb(Sensob):

    def __init__(self):
        self.sensor=irproximity_sensor.IRProximitySensor()

    def update(self):
        self.sensor.update()

    def get_value(self):
        return self.sensor.get_value()

    def reset(self):
        self.sensor.reset()

class ReflectanceSensOb(Sensob):


    #her brukes max og min for å kalibrere, kan evt sette auto_calibrate til TRUE for auto-kalibrering
    def __init__(self):
<<<<<<< HEAD
=======
        self.sensor=reflectance_sensors.ReflectanceSensors(auto_calibrate=False,min_reading=100,max_reading=1000)
        self.get_value()

    def update(self):
        self.updated_value=self.sensor.update()

    def get_value(self):
        self.value=self.sensor.get_value()
        return self.value

    def reset(self):
        self.sensor.reset()

class CameraSensob(Sensob):

    def __init__(self):
>>>>>>> master
        self.sensor=camera.Camera(img_width=128,img_height=96,img_rot=0)

    def update(self):
        self.sensor.update()

    def get_value(self):
        self.value=self.sensor.get_value()
        return self.value

    def reset(self):
        self.sensor.reset()


    def dominant_color_in_picture(self):  #returnerer den dominerende fargen i et bilde(RGB)

        image=Imager(image=self.get_value())
        image=image.resize(70,70)

        image_width=70
        image_height=70

        R_value=0
        G_value=0
        B_value=0

        self.greatest_color_value=''

        #regner ut gjennomsnittsverdien i pi
        for i in range(0,image_width):
            for x in range(image_height):
                R=image.get_pixel(i,x)
                G=image.get_pixel(i,x)
                B=image.get_pixel(i,x)

                R_value=(R+R_value)/2
                G_value=(G+G_value)/2
                B_value=(B+B_value)/2

        if R_value>=G_value and R_value>=B_value:
            self.greatest_color_value='red'

        elif G_value>=R_value and G_value>=B_value:
            self.greatest_color_value='green'

        elif B_value>=R_value and B_value>=G_value:
            self.greatest_color_value='blue'

        else:
            self.greatest_color_value='undesided'

        return self.greatest_color_value












