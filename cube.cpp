//  cube.cpp - Library for grippers control           @kas 2014

#include "Arduino.h"
#include <VarSpeedServo.h>
#include "cube.h"

#define    SEIZE         12 //12 //8 //10 //12     // angle bias for seizing cube w/o pressure

Cube::Cube(int downPinch_pin, int downRot_pin, int backPinch_pin, int backRot_pin)  {
  _downPinch_pin = downPinch_pin;
  _downRot_pin = downRot_pin;
  _backPinch_pin = backPinch_pin;
  _backRot_pin = backRot_pin;
}

void Cube::begin(int speed)  {
  _downPinch_servo.attach(_downPinch_pin, 1000, 2000);             // modified by richimoeller, values were used during position finding
  _downRot_servo.attach(_downRot_pin, 520, 2620);                  // default min is 544, max is 2400; modified by richimoeller
  _backPinch_servo.attach(_backPinch_pin, 1000, 2000);             // modified by richimoeller, values were used during position finding
  _backRot_servo.attach(_backRot_pin, 520, 2620);                  // default min is 544, max is 2400; modified by richimoeller

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

  downArmCenter();
  backArmCenter();
}

void Cube::downSetLimits(int Close, int Open, int CW, int Mid, int CCW)  {
  _downClose = Close;
  _downOpen = Open;
  _downCW = CW;
  _downCCW = CCW;
  _downMid = Mid;
}

void Cube::backSetLimits(int Close, int Open, int CW, int Mid, int CCW)  {
  _backClose = Close;
  _backOpen = Open;
  _backCW = CW;
  _backCCW = CCW;
  _backMid = Mid;
  downArmCenter();
  backArmCenter();
}

void Cube::setSpeed(int speed)  {
  _speed = speed;
}

// -------------------------------------------------------------------------

void Cube::seize()  {
  _downPinch_servo.write(_downClose + SEIZE, _speed, false);
  _backPinch_servo.write(_backClose + SEIZE, _speed, true);
}

void Cube::grip()  {
  _downPinch_servo.write(_downClose, 100, true);
  _backPinch_servo.write(_backClose, 100, true);
}



void Cube::gripSoft()  {
  _downPinch_servo.write(_downClose + SEIZE - 2, _speed, false);
  _backPinch_servo.write(_backClose + SEIZE - 2, _speed, true);
}

void Cube::reseat()  {
  _downPinch_servo.write(_downClose + SEIZE + 4, 100, false);
  _backPinch_servo.write(_backClose + SEIZE + 4, 100, true);
  delay(50);
  _downPinch_servo.write(_downClose, 100, false);
  _backPinch_servo.write(_backClose, 100, true);
}

void Cube::free()  {
  _downPinch_servo.write(_downClose + SEIZE + 2, 100, false);
  _backPinch_servo.write(_backClose + SEIZE + 2, 100, true);
}


//  ----< Move functions (F R B L U D) >-----------------------------

void Cube::Fr()    {
  Fr(1);
}
void Cube::Fr2()   {
  Fr(2);
}
void Cube::Frp()   {
  Fr(3);
}

void Cube::L()     {
  L(1);
}
void Cube::L2()    {
  L(2);
}
void Cube::Lp()    {
  L(3);
}

void Cube::R()     {
  R(1);
}
void Cube::R2()    {
  R(2);
}
void Cube::Rp()    {
  R(3);
}

void Cube::U()     {
  U(1);
}
void Cube::U2()    {
  U(2);
}
void Cube::Up()    {
  U(3);
}

void Cube::D()     {
  D(1);
}
void Cube::D2()    {
  D(2);
}
void Cube::Dp()    {
  D(3);
}

void Cube::B()     {
  B(1);
}
void Cube::B2()    {
  B(2);
}
void Cube::Bp()    {
  B(3);
}

void Cube::D(int type)  {             // 1:"D"  2:"D2"  3:"D'"
  grip();
  if      (type == 1)    downArmCW();
  else if (type == 2)  {
    downArmCW();
    downArm_OpenCenterClose();
    delay(200);
    downArmCW();
  }
  else if (type == 3)    downArmCCW();
  downArm_OpenCenterClose();
//  reseat();
}

void Cube::B(int type)  {
  grip();
  if      (type == 1)    backArmCW();
  else if (type == 2)  {
    backArmCW();
    backArm_OpenCenterClose();
    delay(200);
    backArmCW();
  }
  else if (type == 3)    backArmCCW();
  backArm_OpenCenterClose();
   // reseat();
}

void Cube::R(int type)  {
  grip();
  backArmOpen_downArmCW_backArmClose();
   // reseat();
  downArm_OpenCenterClose();
   // reseat();
  B(type);
  backArmOpen_downArmCCW_backArmClose();
   // reseat();
  downArm_OpenCenterClose();
   // reseat();
}

void Cube::L(int type)  {
  grip();
  backArmOpen_downArmCCW_backArmClose();
  downArm_OpenCenterClose();
   // reseat();
  B(type);
  backArmOpen_downArmCW_backArmClose();
  downArm_OpenCenterClose();
   // reseat();
}

void Cube::U(int type)  {
  grip();
  downArmOpen_backArmCW_downArmClose();
  backArm_OpenCenterClose();
  downArmOpen_backArmCW_downArmClose();
  backArm_OpenCenterClose();
   // reseat();
  D(type);
  downArmOpen_backArmCW_downArmClose();
  backArm_OpenCenterClose();
  downArmOpen_backArmCW_downArmClose();
  backArm_OpenCenterClose();
   // reseat();
}

void Cube::Fr(int type)  {
  grip();
  backArmOpen_downArmCW_backArmClose();
   // reseat();
  downArm_OpenCenterClose();
   // reseat();
  backArmOpen_downArmCW_backArmClose();
   // reseat();
  downArm_OpenCenterClose();
   // reseat();
  B(type);
  backArmOpen_downArmCW_backArmClose();
   // reseat();
  downArm_OpenCenterClose();
   // reseat();
  backArmOpen_downArmCW_backArmClose();
   // reseat();
  downArm_OpenCenterClose();
   // reseat();
}




//  ----< Scan functions (f r b l u d) >-----------------------------
// richimoeller: entered a delay of 500ms here to allow for a clean color recognition shot
void Cube::scanBack()  {
  delay(500);
  y(1);

//  grip();
// gripSoft();
}

void Cube::scanLeft()  {
  delay(500);
  y(1);
}

void Cube::scanFront()  {
  delay(500);
  y(1);
}

void Cube::scanRight()  {
  delay(500);
  x(3);
}

void Cube::scanUp()  {
  delay(500);
  x(2);
}

void Cube::scanDown()  {
  delay(500);
  x(3);
  y(3);
}

void Cube::scanFront2()  {
 // x(3);
 // y(3);
}

//  x : rotate the entire Cube in the direction of R
//  y : rotate the entire Cube in the direction of U
//  z : rotate the entire Cube in the direction of F

void Cube::x(int type)  {             // type=1:"x"  2:"x2"  3:"x'"
  grip();
  backArmOpen_downArmCCW_backArmClose();
  downArmOpen();
  downArmCenter();
  if      (type == 1)    backArmCCW();
  else if (type == 2)    {
    backArmCW();
    downArmClose();
    backArm_OpenCenterClose();
    downArmOpen();
    backArmCW();
  }
  else if (type == 3)    backArmCW();
  downArmClose();
  backArmOpen();
  backArmCenter();
  downArmCW();
  backArmClose();
  downArm_OpenCenterClose();
  reseat();
  gripSoft();
}

void Cube::y(int type)  {
  grip();
  if      (type == 1)    backArmOpen_downArmCCW_backArmClose();
  else if (type == 3)    backArmOpen_downArmCW_backArmClose();
  downArm_OpenCenterClose();
  reseat();
  gripSoft();
}

void Cube::z(int type)  {
  grip();
  if      (type == 1)    downArmOpen_backArmCCW_downArmClose();
  else if (type == 3)    downArmOpen_backArmCW_downArmClose();
  backArm_OpenCenterClose();
  reseat();
  gripSoft();
}



//  ----< Utilities (private) >-----------------------------
void Cube::downArmCW()  {
  _downRot_servo.write(_downCW -3, _speed, true);   // create slight overshot
  _downRot_servo.write(_downCW, _speed, true);
}



void Cube::downArmCCW()  {
  _downRot_servo.write(_downCCW, _speed, true);
}

void Cube::downArmCenter()  {
  _downRot_servo.write(_downMid, _speed, true);
}

void Cube::backArmCW()  {
  _backRot_servo.write(_backCW -2, _speed, true);   // create slight overshot
  _backRot_servo.write(_backCW, _speed, true);
}

void Cube::backArmCCW()  {
  _backRot_servo.write(_backCCW, _speed, true);
}

void Cube::backArmCenter()  {
  _backRot_servo.write(_backMid, _speed, true);
}

void Cube::downArmOpen()  {
  _downPinch_servo.write(_downOpen, _speed, true);
}

void Cube::downArmClose()  {
  _downPinch_servo.write(_downClose, _speed, true);
}

void Cube::backArmOpen()  {
  _backPinch_servo.write(_backOpen, _speed, true);
}

void Cube::backArmClose()  {
  _backPinch_servo.write(_backClose, _speed, true);
}

void Cube::downArm_OpenCenterClose()  {
  downArmOpen();
  downArmCenter();
  downArmClose();
  reseat();
}

void Cube::backArm_OpenCenterClose()  {
  backArmOpen();
  backArmCenter();
  backArmClose();
  reseat();
}

void Cube::backArmOpen_downArmCW_backArmClose()  {
  backArmOpen();
  downArmCW();
  backArmClose();
  reseat();
}

void Cube::backArmOpen_downArmCCW_backArmClose()  {
  backArmOpen();
  downArmCCW();
  backArmClose();
  reseat();
}

void Cube::downArmOpen_backArmCW_downArmClose()  {
  downArmOpen();
  backArmCW();
  downArmClose();
  reseat();
}

void Cube::downArmOpen_backArmCCW_downArmClose()  {
  downArmOpen();
  backArmCCW();
  downArmClose();
  reseat();
}
