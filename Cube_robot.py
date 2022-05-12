import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time
import numpy as np
from gpiozero import AngularServo




class Cube: 

    #define GPIO pins

    #STEPPER MOTORS PIN IN
    #downRotPin
    STEP_A_PIN_DIRECTION = 22 # Direction (DIR) GPIO Pin
    STEP_A_PIN_STEP = 23 # Step GPIO Pin

    #backRotPin
    STEP_B_PIN_DIRECTION = 22#  Direction (DIR) GPIO Pin
    STEP_B_PIN_STEP = 23 # Step GPIO Pin

    #SERVO MOTORS PIN IN
    SERVO_A_DIGITAL_PIN = 6 #downPinchPin
    SERVO_B_DIGITAL_PIN = 2 #backPinchPin

    SEIZE = 12

    def delay(seconds):
        time.sleep(seconds)

    def toStep(self,degrees):
        return (degrees/1.8) #Stepper resolution

    def begin(self, speed):
        servo_a = AngularServo(SERVO_A_DIGITAL_PIN, min_pulse_width=0.0006, max_pulse_width=0.0023)servo_b = Servo(SERVO_A_DIGITAL_PIN)
        servo_b = AngularServo(SERVO_B_DIGITAL_PIN, min_pulse_width=0.0006, max_pulse_width=0.0023)servo_b = Servo(SERVO_A_DIGITAL_PIN)
        
        step_a = RpiMotorLib.A4988Nema(STEP_A_PIN_DIRECTION, STEP_A_PIN_STEP, (17,17,17), "DRV8825")
        step_b = RpiMotorLib.A4988Nema(STEP_B_PIN_DIRECTION, STEP_B_PIN_STEP, (17,17,17), "DRV8825")

        // GRADOS

        _downClose = 52
        _downOpen = 125
        _downCW = 176
        _downCCW = 7
        _downMid = 92
        _backClose = 35
        _backOpen = 115
        _backCW = 173
        _backCCW = 4
        _backMid = 88
        _speed = speed

        downArmCenter()
        backArmCenter()
        
    # write(value, speed, wait) - wait is a boolean 
    # that, if true, causes the function call to block
    # until move is complete
    
    def downSetLimits(self,Close,Open,CW,Mid,CCW):
        _downClose = Close
        _downOpen = Open
        _downCW = CW
        _downCCW = CCW
        _downMid = Mid

    def backSetLimits(self,Close,Open,CW,Mid,CCW):
        _backClose = Close
        _backOpen = Open
        _backCW = CW
        _backCCW = CCW
        _backMid = Mid
        downArmCenter()
        backArmCenter()
    
    def grip(self):
        servo_a.angle = _downClose
        servo_b.angle = _downClose

    def seize(self):
        servo_a.angle = _downClose + SEIZE
        servo_b.angle = _backClose  + SEIZE

    def reseat(self):
        servo_a.angle = _downClose + SEIZE + 4
        servo_b.angle = _backClose + SEIZE + 4
        delay(50)
        servo_a.angle = _downClose
        servo_b.angle = _backClose 

    def gripSoft(self):
        servo_a.angle = _downClose + SEIZE - 2
        servo_b.angle = _backClose + SEIZE - 2

    def free(self):
        servo_a.angle = _downClose + SEIZE + 2
        servo_b.angle = _backClose + SEIZE + 2


    #rubik sides

    def D(self,type):
        grip();
        if (type == 1):
            downArmCW()
        elif (type == 2):
            downArmCW()
            downArm_OpenCenterClose()
            delay(200)
            downArmCW()
        
        elif (type == 3):
            downArmCCW()

        downArm_OpenCenterClose()

    def B(self,type):
        grip()
        if (type == 1):
            backArmCW()
        elif (type == 2):
            backArmCW()
            backArm_OpenCenterClose()
            delay(200)
            backArmCW()
        
        elif (type == 3):
           downArmCCW()

        backArm_OpenCenterClose()

    def R(self, type):
        grip()
        backArmOpen_downArmCW_backArmClose()
        downArm_OpenCenterClose()
        B(type)
        backArmOpen_downArmCCW_backArmClose()
        downArm_OpenCenterClose()


    def L(self , type):
        grip()
        backArmOpen_downArmCCW_backArmClose()
        downArm_OpenCenterClose()
        B(type)
        backArmOpen_downArmCW_backArmClose()
        downArm_OpenCenterClose()

    def U(self, type):
        grip();
        downArmOpen_backArmCW_downArmClose()
        backArm_OpenCenterClose()
        downArmOpen_backArmCW_downArmClose()
        backArm_OpenCenterClose()
        D(type)
        downArmOpen_backArmCW_downArmClose()
        backArm_OpenCenterClose()
        downArmOpen_backArmCW_downArmClose()
        backArm_OpenCenterClose()

    def Fr(self, type):
        grip();
        backArmOpen_downArmCW_backArmClose();
        downArm_OpenCenterClose();
        backArmOpen_downArmCW_backArmClose();
        downArm_OpenCenterClose();
        B(type);
        backArmOpen_downArmCW_backArmClose();
        downArm_OpenCenterClose();
        backArmOpen_downArmCW_backArmClose();
        downArm_OpenCenterClose();


#  ----< Scan functions (f r b l u d) >-----------------------------

    def scanBack(self):
        delay(0.5)
        y(1)

    def scanLeft(self):
        delay(0.5)
        y(1)

    def scanFront(self):
        delay(0.5)
        y(1)

    def scanRight(self):
        delay(0.5)
        x(3)

    def scanUp(self):
        delay(0.5)
        x(2)
    

    def scanDown(self):
        delay(0.5)
        x(3)
        y(3)
    

    def x(type):
        grip()
        backArmOpen_downArmCCW_backArmClose()
        downArmOpen()
        downArmCenter()
        if (type == 1):
            backArmCCW()

        elif (type == 2):    {
            backArmCW()
            downArmClose()
            backArm_OpenCenterClose()
            downArmOpen()
            backArmCW()
        }
        elif (type == 3):
            backArmCW()
            downArmClose()
            backArmOpen()
            backArmCenter()
            downArmCW()
            backArmClose()
            downArm_OpenCenterClose()
            reseat()
            gripSoft()

    def y(type):
        grip()
        if(type == 1):
            backArmOpen_downArmCCW_backArmClose()
        elif (type == 3):
            backArmOpen_downArmCW_backArmClose()
            downArm_OpenCenterClose()
            reseat()
            gripSoft()

    def z(type):
        grip()
        if(type == 1):
            downArmOpen_backArmCCW_downArmClose()
        elif (type == 3):
            downArmOpen_backArmCW_downArmClose()
            backArm_OpenCenterClose()
            reseat()
            gripSoft()


    def downArmCenter(self):
        step_a.motor_go(
            False, # True=Clockwise, False=Counter-Clockwise
            "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
            toStep(_downMid), # number of steps
            .0005, # step delay [sec]
            False, # True = print verbose output 
            .05
        ) # initial delay [sec]

    def backArmCCW(self):
        step_a.motor_go(
            False, # True=Clockwise, False=Counter-Clockwise
            "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
            toStep(_backCCW), # number of steps
            .0005, # step delay [sec]
            False, # True = print verbose output 
            .05
        ) # initial delay [sec]


    def backArmCCW(self):
        step_a.motor_go(
            False, # True=Clockwise, False=Counter-Clockwise
            "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
            toStep(_downCW -3), # number of steps
            .0005, # step delay [sec]
            False, # True = print verbose output 
            .05
        ) # initial delay [sec]
        step_a.motor_go(
            False, # True=Clockwise, False=Counter-Clockwise
            "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
            toStep(_downCW), # number of steps
            .0005, # step delay [sec]
            False, # True = print verbose output 
            .05
        ) # initial delay [sec]

    def backArmCCW(self):
        step_a.motor_go(
            False, # True=Clockwise, False=Counter-Clockwise
            "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
            toStep(_backCW -2), # number of steps
            .0005, # step delay [sec]
            False, # True = print verbose output 
            .05
        ) # initial delay [sec]
        step_a.motor_go(
            False, # True=Clockwise, False=Counter-Clockwise
            "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
            toStep(_backCW), # number of steps
            .0005, # step delay [sec]
            False, # True = print verbose output 
            .05
        ) # initial delay [sec]

    def downArmCCW(self):
        step_b.motor_go(
            False, # True=Clockwise, False=Counter-Clockwise
            "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
            toStep(_downCCW), # number of steps
            .0005, # step delay [sec]
            False, # True = print verbose output 
            .05
        ) # initial delay [sec]

    def downArmCenter(self):
        step_b.motor_go(
            False, # True=Clockwise, False=Counter-Clockwise
            "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
            toStep(_downMid), # number of steps
            .0005, # step delay [sec]
            False, # True = print verbose output 
            .05
        ) # initial delay [sec]

    def downArmOpen(self):
        servo_a.angle = _downOpen

    def downArmOpen(self):
        servo_a.angle = _downClose

    def backArmOpen(self):
        servo_b.angle = _backOpen

    def backArmClose(self):
        servo_b.angle = _backClose

    def downArm_OpenCenterClose(self):
        downArmOpen()
        downArmCenter()
        downArmClose()
        reseat()


    def backArm_OpenCenterClose(self):
        backArmOpen()
        backArmCenter()
        backArmClose()
        reseat()

    def backArmOpen_downArmCW_backArmClose(self):
        backArmOpen()
        downArmCW()
        backArmClose()
        reseat()

    def backArmOpen_downArmCW_backArmClose(self):
        backArmOpen()
        downArmCCW()
        backArmClose()
        reseat()

    def downArmOpen_backArmCW_downArmClose(self):
        downArmOpen()
        backArmCW()
        downArmClose()
        reseat()

    def downArmOpen_backArmCCW_downArmClose(self):
        downArmOpen()
        backArmCCW()
        downArmClose()
        reseat()