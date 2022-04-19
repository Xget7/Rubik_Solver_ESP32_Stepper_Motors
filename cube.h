//  cube.h - Library for grippers control           @kas 2014

#ifndef Cube_h
#define Cube_h

#include "Arduino.h"
#include <VarSpeedServo.h> 

class Cube  {

  public:
     Cube(int downPinch_pin, int downRot_pin, int backPinch_pin, int backRot_pin);
     void begin(int speed);
     void downSetLimits(int Close, int Open, int CW, int Mid, int CCW);
     void backSetLimits(int Close, int Open, int CW, int Mid, int CCW);
     void setSpeed(int speed);

     void seize();                    // hold cube without pressure
     void grip();                     // hold cube with high pressure
     void gripSoft();                 // hold cube with low pressure
     void free();                     // release pressure
     void reseat();                   // open/close pinch

     void scanFront();                //Moves for scanning
     void scanLeft();
     void scanBack();
     void scanRight();
     void scanUp();
     void scanDown();
     void scanFront2();

     void L();
     void L2();
     void Lp();
    
     void R();
     void R2();
     void Rp();
    
     void U();
     void U2();
     void Up();
    
     void D();
     void D2();
     void Dp();
    
     void Fr();
     void Fr2();
     void Frp();
    
     void B();
     void B2();
     void Bp();

  private:
     VarSpeedServo _downPinch_servo;     // create servo objects
     VarSpeedServo _downRot_servo; 
     VarSpeedServo _backPinch_servo;
     VarSpeedServo _backRot_servo; 

     int _downPinch_pin;
     int _downRot_pin;
     int _backPinch_pin;
     int _backRot_pin;

     int _downClose;
     int _downOpen;
     int _downCW;
     int _downCCW;
     int _downMid;
     int _backClose;
     int _backOpen;
     int _backCW;
     int _backCCW;
     int _backMid;
     int _speed;

     void y(int type);
     void x(int type);
     void z(int type);

     void B(int type);                  // Moves for solving
     void D(int type);
     void R(int type);
     void L(int type);
     void U(int type);
     void Fr(int type);

     void downArmOpen();
     void downArmClose();
     void downArmCW();
     void downArmCCW();
     void downArmCenter();
     void backArmOpen();
     void backArmClose();
     void backArmCW();
     void backArmCCW();
     void backArmCenter();
     void downArm_OpenCenterClose();
     void backArm_OpenCenterClose();
     void downArmOpen_backArmCW_downArmClose();
     void downArmOpen_backArmCCW_downArmClose();
     void backArmOpen_downArmCW_backArmClose();
     void backArmOpen_downArmCCW_backArmClose();
};
#endif
