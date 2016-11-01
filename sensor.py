__author__ = 'mattisaraya'


import RPi.GPIO as GPIO
import time

from ultrasonic import Ultrasonic
from irproximity_sensor import IRProximitySensor
from camera import Camera
from imager2 import Imager
from reflectance_sensors import ReflectanceSensors

class Sensob():

    value=0

    def __init__(self):
        self.camera_value=0
        self.irproximity_value=0
        self.ultrasoinc_value=0
        self.reflector_value=0






    def sensob_update(self):
        self.camera_value=Camera.get_value()
        self.irproximity_value=IRProximitySensor.get_value()
        self.ultrasoinc_value=Ultrasonic.get_value()
        self.reflector_value=ReflectanceSensors.get_value()

    def sensob_reset(self):
        self.camera_value=Ultrasonic.reset()
        self.irproximity_value=IRProximitySensor.reset()
        self.ultrasoinc_value=Ultrasonic.reset()
        self.reflector_value=ReflectanceSensors.reset()





