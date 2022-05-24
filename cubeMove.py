import time
from RpiMotorLib import RpiMotorLib
from gpiozero import AngularServo


class Cube_Move:
    def __init__(self):
        # STEPPER MOTORS PIN IN
        # downRotPin
        self.STEP_A_PIN_DIRECTION = 17
        self.STEP_A_PIN_STEP = 27

        # backRotPin
        self.STEP_B_PIN_DIRECTION = 26
        self.STEP_B_PIN_STEP = 6

        # SERVO MOTORS PIN IN
        self.SERVO_A_DIGITAL_PIN = 13
        self.SERVO_B_DIGITAL_PIN = 19
        self.SEIZE = 12


    def delay(seconds):
        time.sleep(seconds)

    def toStep(self, degrees):
        return int((degrees/1.8))  # Stepper resolution

    def begin(self, speed):
        self.servo_a = AngularServo(
            self.SERVO_A_DIGITAL_PIN, min_pulse_width=0.0006, max_pulse_width=0.0023)
        self.servo_b = AngularServo(
            self.SERVO_B_DIGITAL_PIN, min_pulse_width=0.0006, max_pulse_width=0.0023)
        self.step_a = RpiMotorLib.A4988Nema(
            self.STEP_A_PIN_DIRECTION, self.STEP_A_PIN_STEP, (17, 17, 17), "DRV8825")
        self.step_b = RpiMotorLib.A4988Nema(
            self.STEP_B_PIN_DIRECTION, self.STEP_B_PIN_STEP, (17, 17, 17), "DRV8825")
        # GRADOS
        self._downClose = 52
        self._downOpen = 125
        self._downCW = 176
        self._downCCW = 7
        self._downMid = 94
        self._backClose = 35
        self._backOpen = 115
        self._backCW = 173
        self._backCCW = 4
        self._backMid = 88
        self._speed = speed

        self.downArmCenter()
        self.backArmCenter()

    # write(value, speed, wait) - wait is a boolean
    # that, if true, causes the function call to block
    # until move is complete

    def downSetLimits(self, Close, Open, CW, Mid, CCW):
        self._downClose = Close
        self._downOpen = Open
        self._downCW = CW
        self._downCCW = CCW
        self._downMid = Mid

    def backSetLimits(self, Close, Open, CW, Mid, CCW):
        self._backClose = Close
        self._backOpen = Open
        self._backCW = CW
        self._backCCW = CCW
        self._backMid = Mid
        self.downArmCenter()
        self.backArmCenter()

    def grip(self):
        print("grip")
        self.servo_a.angle = self._downClose
        self.servo_b.angle = self._downClose

    def seize(self):
        print("Seize ")
        self.servo_a.angle = self._downClose + self.SEIZE
        self.servo_b.angle = self._backClose  + self.SEIZE

    def reseat(self):
        print("Reseat")
        self.servo_a.angle = self._downClose + self.SEIZE + 4
        self.servo_b.angle = self._backClose + self.SEIZE + 4
        self.delay(50)
        self.servo_a.angle = self._downClose
        self.servo_b.angle = self._backClose

    def gripSoft(self):
        print(f" GripSoft {self._downClose} + {self.SEIZE - 2}")
        self.servo_a.angle = self._downClose + self.SEIZE - 2
        self.servo_b.angle = self._backClose + self.SEIZE - 2

    def free(self):
        print(f" Free {self._downClose} + {self.SEIZE + 2}")
        self.servo_a.angle = self._downClose + self.SEIZE + 2
        self.servo_b.angle = self._backClose + self.SEIZE + 2

    # rubik sides

    def D(self, type):
        self.grip()
        if (type == 1):
            self.downArmCW()
        elif (type == 2):
            self.downArmCW()
            self.downArm_OpenCenterClose()
            self.delay(200)
            self.downArmCW()

        elif (type == 3):
            self.downArmCCW()

        self.downArm_OpenCenterClose()

    def B(self, type):
        self.grip()
        if (type == 1):
            self.backArmCW()
        elif (type == 2):
            self.backArmCW()
            self.backArm_OpenCenterClose()
            self.delay(200)
            self.backArmCW()

        elif (type == 3):
            self.downArmCCW()

        self.backArm_OpenCenterClose()

    def R(self, type):
        self.grip()
        self.backArmOpen_downArmCW_backArmClose()
        self.downArm_OpenCenterClose()
        self.B(type)
        self.backArmOpen_downArmCCW_backArmClose()
        self.downArm_OpenCenterClose()

    def L(self, type):
        self.grip()
        self.backArmOpen_downArmCCW_backArmClose()
        self.downArm_OpenCenterClose()
        self.B(type)
        self.backArmOpen_downArmCW_backArmClose()
        self.downArm_OpenCenterClose()

    def U(self, type):
        self.grip()
        self.downArmOpen_backArmCW_downArmClose()
        self.backArm_OpenCenterClose()
        self.downArmOpen_backArmCW_downArmClose()
        self.backArm_OpenCenterClose()
        self.D(type)
        self.downArmOpen_backArmCW_downArmClose()
        self.backArm_OpenCenterClose()
        self.downArmOpen_backArmCW_downArmClose()
        self.backArm_OpenCenterClose()

    def Fr(self, type):
        self.grip()
        self.backArmOpen_downArmCW_backArmClose()
        self.downArm_OpenCenterClose()
        self.backArmOpen_downArmCW_backArmClose()
        self.downArm_OpenCenterClose()
        self.B(type)
        self.backArmOpen_downArmCW_backArmClose()
        self.downArm_OpenCenterClose()
        self.backArmOpen_downArmCW_backArmClose()
        self.downArm_OpenCenterClose()


#  ----< Scan functions (f r b l u d) >-----------------------------

    def scanBack(self):
        self.delay(0.5)
        self.y(1)

    def scanLeft(self):
        self.delay(0.5)
        self.y(1)

    def scanFront(self):
        self.delay(0.5)
        self.y(1)

    def scanRight(self):
        self.delay(0.5)
        self.x(3)

    def scanUp(self):
        self.delay(0.5)
        self.x(2)

    def scanDown(self):
        self.delay(0.5)
        self.x(3)
        self.y(3)

    def x(self, type):
        self.grip()
        self.backArmOpen_downArmCCW_backArmClose()
        self.downArmOpen()
        self.downArmCenter()
        if (type == 1):
            self.backArmCCW()

        elif (type == 2):
            self.backArmCW()
            self.downArmClose()
            self.backArm_OpenCenterClose()
            self.downArmOpen()
            self.backArmCW()

        elif (type == 3):
            self.backArmCW()
            self.downArmClose()
            self.backArmOpen()
            self.backArmCenter()
            self.downArmCW()
            self.self.backArmClose()
            self.downArm_OpenCenterClose()
            self.reseat()
            self.gripSoft()

    def y(self, type):
        self.self.grip()
        if(type == 1):
            self.self.backArmOpen_downArmCCW_backArmClose()
        elif (type == 3):
            self.self.backArmOpen_downArmCW_backArmClose()
            self.self.downArm_OpenCenterClose()
            self.self.reseat()
            self.self.gripSoft()

    def z(self, type):
        self.grip()
        if(type == 1):
            self.self.downArmOpen_backArmCCW_downArmClose()
        elif (type == 3):
            self.self.downArmOpen_backArmCW_downArmClose()
            self.self.backArm_OpenCenterClose()
            self.self.reseat()
            self.self.gripSoft()

    def backArmCenter(self):
        print(f"{self.step_a} backArmCenter")
        self.step_a.motor_go(
            False,  # True=Clockwise, False=Counter-Clockwise
            "Full",  # Step type (Full,Half,1/4,1/8,1/16,1/32)
            self.toStep(self._downMid),  # number of steps
            .0005,  # step delay [sec]
            False,  # True = print verbose output
            .05
        )  # initial delay [sec]

    def backArmCCW(self):
        print(f"{self.step_b} + {self.step_a}  backArmCCW")
        self.step_b.motor_go(
             True, # True=Clockwise, False=Counter-Clockwise
             "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
             self.toStep(self._backCCW), # number of steps
             .0005, # step delay [sec]
             False, # True = print verbose output
             .05
         ) # initial delay [sec]
        self.step_a.motor_go(
             False, # True=Clockwise, False=Counter-Clockwise
             "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
             self.toStep(self._backCCW), # number of steps
             .0005, # step delay [sec]
             False, # True = print verbose output
             .05
         ) # initial delay [sec]

    def downArmCW(self):
        print(f"{self.step_a }downArmCW")
        self.step_a.motor_go(
             False, # True=Clockwise, False=Counter-Clockwise
             "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
             self.toStep(self._downCW -3), # number of steps
             .0005, # step delay [sec]
            False, # True = print verbose output
             .05
         ) # initial delay [sec]
        self.step_a.motor_go(
             False, # True=Clockwise, False=Counter-Clockwise
             "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
             self.toStep(self._downCW), # number of steps
             .0005, # step delay [sec]
             False, # True = print verbose output
             .05
         ) # initial delay [sec]

    def backArmCW(self):
        print(f"{self.step_a}backArmCW")
        self.step_a.motor_go(
             False, # True=Clockwise, False=Counter-Clockwise
             "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
             self.toStep(self._backCW -2), # number of steps
             .0005, # step delay [sec]
             False, # True = print verbose output
             .05
         ) # initial delay [sec]
        self.step_a.motor_go(
             False, # True=Clockwise, False=Counter-Clockwise
             "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
             self.toStep(self._backCW), # number of steps
             .0005, # step delay [sec]
             False, # True = print verbose output
             .05
         ) # initial delay [sec]

    def downArmCCW(self):
        print(f"{self.step_b} downArmCCW")
        self.step_b.motor_go(
             False, # True=Clockwise, False=Counter-Clockwise
             "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
             self.toStep(self._downCCW), # number of steps
             .0005, # step delay [sec]
             False, # True = print verbose output
             .05
         ) # initial delay [sec]

    def downArmCenter(self):
        print(f"{self.step_b} downArmCenter")
        self.step_b.motor_go(
            False,  # True=Clockwise, False=Counter-Clockwise
            "Full",  # Step type (Full,Half,1/4,1/8,1/16,1/32)
            self.toStep(self._downMid),  # number of steps
            .0005,  # step delay [sec]
            False,  # True = print verbose output
            .05
        )  # initial delay [sec]

    def downArmOpen(self):
        print(f"{self.servo_a} downArmOpen Servo")
        self.servo_a.angle = self._downOpen

    def downArmClose(self):
        print(f"{self.servo_b} downArmClose Servo")
        self.servo_a.angle = self._downClose

    def backArmOpen(self):
        print(f"{self.servo_b} backArmOpen Servo")
        self.servo_b.angle = self._backOpen

    def backArmClose(self):
        print(f"{self.servo_b} + backArmClose Servo")
        self.servo_b.angle = self._backClose

    def downArm_OpenCenterClose(self):
        self.downArmOpen()
        self.downArmCenter()
        self.downArmClose()
        self.reseat()

    def backArm_OpenCenterClose(self):
        self.backArmOpen()
        self.backArmCenter()
        self.backArmClose()
        self.reseat()

    def backArmOpen_downArmCW_backArmClose(self):
        self.backArmOpen()
        self.downArmCW()
        self.backArmClose()
        self.reseat()

    def backArmOpen_downArmCW_backArmClose(self):
        self.backArmOpen()
        self.downArmCCW()
        self.backArmClose()
        self.reseat()

    def downArmOpen_backArmCW_downArmClose(self):
        self.downArmOpen()
        self.backArmCW()
        self.downArmClose()
        self.reseat()

    def downArmOpen_backArmCCW_downArmClose(self):
        self.downArmOpen()
        self.backArmCCW()
        self.downArmClose()
        self.reseat()


cube = Cube_Move().begin(1)
time.sleep(3)
cube.grip()