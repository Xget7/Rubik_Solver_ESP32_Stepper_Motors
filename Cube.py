import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time
import numpy as np
from gpiozero import AngularServo

#define GPIO pins

#STEPPER MOTORS PIN IN
STEP_A_PIN_DIRECTION = 22 # Direction (DIR) GPIO Pin
STEAP_A_PIN_STEP = 23 # Step GPIO Pin

STEP_B_PIN_DIRECTION = 22#  Direction (DIR) GPIO Pin
STEAP_B_PIN_STEP = 23 # Step GPIO Pin

#SERVO MOTORS PIN IN
SERVO_A_DIGITAL_PIN = 6
SERVO_B_DIGITAL_PIN = 2





step_a.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                     "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                     200, # number of steps
                     .0005, # step delay [sec]
                     False, # True = print verbose output 
                     .05) # initial delay [sec]


class Cube: 
    def begin(self, speed):
        servo_a = AngularServo(SERVO_A_DIGITAL_PIN, min_pulse_width=0.0006, max_pulse_width=0.0023)servo_b = Servo(SERVO_A_DIGITAL_PIN)
        servo_b = AngularServo(SERVO_B_DIGITAL_PIN, min_pulse_width=0.0006, max_pulse_width=0.0023)servo_b = Servo(SERVO_A_DIGITAL_PIN)
        step_a = RpiMotorLib.A4988Nema(STEP_A_PIN_DIRECTION, STEAP_A_PIN_STEP, (17,17,17), "DRV8825")
        step_b = RpiMotorLib.A4988Nema(STEP_B_PIN_DIRECTION, STEAP_B_PIN_STEP, (17,17,17), "DRV8825")

        // GRADOS

        _downClose = 52;
        _downOpen = 125;
        _downCW = 176;
        _downCCW = 7;
        _downMid = 92;
        _backClose = 35;
        _backOpen = 115;
        _backCW = 173;
        _backCCW = 4;
        _backMid = 88;
        _speed = speed;
        
    def grip(self):
        pass
    


