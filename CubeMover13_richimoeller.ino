#define VERSION       "Cube Mover V1.3  @kas2014\n"

// V1.3:  added reseat(),  slight overshot in xxArmCW() - Maker faire 2017 release
// V1.2:  refactored using Cube class - Posted
// V1.1:  replaced Servo with VarSpeedServo library 
// V1.0:  initial release

//Exposure:
//Si Jaune reconnu comme blanc ou orange reconnu comme jaune: diminuer l'expo (-4 >> -6)
//Si Jaune reconnu comme orange: augmenter l'expo (-6 >> -4)

#include <VarSpeedServo.h> 
#include "cube.h"
#include <SoftwareSerial.h>
// ---------- user adjustments -------------------
#define    DOWN_CLOSE          49
#define    DOWN_OPEN          125
#define    DOWN_CW            178
#define    DOWN_MID            93
#define    DOWN_CCW             5

#define    BACK_CLOSE          31
#define    BACK_OPEN          115
#define    BACK_CW            175
#define    BACK_MID            88
#define    BACK_CCW             2

#define    LOW_SPEED           50
#define    HI_SPEED            80
// -----------------------------------------------

#define    downPinchPin        10
#define    downRotPin          11
#define    backPinchPin         8
#define    backRotPin           9
#define    bipPin               4             // buzzer
#define    myRX                 6
#define    myTX                 7
#define    ledPin              13

#define    STX               0x02             // serial data frame delimiters
#define    ETX               0x03

SoftwareSerial mySerial(myRX, myTX); 

boolean    DEBUG_SERIAL =         false;

Cube myCube(downPinchPin, downRotPin, backPinchPin, backRotPin);

char cmd[128];                                 // bytes received buffer

void setup() {
  Serial.begin(57600);
  mySerial.begin(9600);   
  //if (DEBUG_SERIAL)      Serial.println(VERSION);
  pinMode(bipPin, OUTPUT);     
  pinMode(ledPin, OUTPUT); 

  myCube.begin(HI_SPEED);                 // set HIGH servo's speed 
  myCube.downSetLimits(DOWN_CLOSE, DOWN_OPEN, DOWN_CW,DOWN_MID, DOWN_CCW); // set limits for pinch and rotation servo's
  myCube.backSetLimits(BACK_CLOSE, BACK_OPEN, BACK_CW, BACK_MID, BACK_CCW);
  myCube.seize();
  //Serial.println("OK bis hierher_1");
  bip(20, 2);                             // bip
}

void loop() {
// myCube.downArmOpen();        // uncomment for checking moves
// myCube.backArmOpen();
// delay(8000);
// myCube.downArmClose();
// myCube.backArmClose();
// delay(8000);
  
  if (DEBUG_SERIAL)  {
    if(getSerialMonitor())    parseData();        // obtain commands from Serial Monitor
  }  else  {
    if(getSerialData())       parseData();        // obtain commands through Bluetooth
  } 
}

// ---------------------------

boolean getSerialData()  {
  if(mySerial.available())  {                                       // data received from smartphone
    delay(2);
    cmd[0] =  mySerial.read();
      if(cmd[0] == STX)  {
      int i=1;      
      while(mySerial.available())  {
        delay(1);
        cmd[i] = mySerial.read();
        if(cmd[i]>'u' || i>124)    {bip(100, 2); return false;}    // Communication error  XXX reinitialiser à zero <<<
        if((cmd[i]==ETX))          {bip(200, 1);  return true; } 
        i++;
      }
    }
    else {bip(100, 3); return false;}
  }
  return false;
}

boolean getSerialMonitor()  {  // Serial Monitor setting: Newline
  if(Serial.available())  {
    for(int i=0; i<124; i++)    cmd[i] = 0;
    int n = Serial.readBytesUntil('\n', cmd, 124);
   cmd[n+1] = ETX;
   return true;
  }
 return false; 
}

void parseData()    { // parseData(cmd)
  int i = 0;
  String progress = "";
  Serial.println(cmd);
  while (cmd[i] != ETX) {
    mySerial.print(cmd[i]); mySerial.print(" ");
//    Serial.println(cmd[i]);
    switch(cmd[i])  {

      // Test commands  --------------------------------------------------------------
//      1: downArmOpen      6: backArmOpen
//      2: downArmClose     7: backArmClose
//      3: downArmCW        8: backArmCW
//      4: downArmCenter    9: backArmCenter
//      5: downArmCCW       0: backArmCCW
//      T: seize     release gripper pressure

/
      // Move commands  ------------------------------------------------------------
      case 'R':                                                    //  'R' moves
        switch(cmd[i+1])  {
          case '2':
            //Serial.print("R2 ");
            myCube.R2();
            break;
          case 39: // ASCII 39: apostrophe character
            //Serial.print("R' ");
            myCube.Rp();
            break;
          default:
            //Serial.print("R ");
            myCube.R();
            break;
        }
        break;
      case 'L':                                                    //  'L' moves
        switch(cmd[i+1])  {
          case '2':
            //Serial.print("L2 ");
            myCube.L2();
            break;
          case 39:
            //Serial.print("L' ");
            myCube.Lp();
            break;
          default:
            //Serial.print("L ");
            myCube.L();
            break;
        }
        break;
      case 'U':                                                    //  'U' moves
        switch(cmd[i+1])  {
          case '2':
            //Serial.print("U2 ");
            myCube.U2();
            break;
          case 39:
            //Serial.print("U' ");
            myCube.Up();
            break;
          default:
            //Serial.print("U ");
            myCube.U();
            break;
        }
        break;
      case 'D':                                                    //  'D' moves
        switch(cmd[i+1])  {
          case '2':
            //Serial.print("D2 ");
            myCube.D2();
            break;
          case 39:
            //Serial.print("D' ");
            myCube.Dp();
            break;
          default:
            //Serial.print("D ");
            myCube.D();
            break;
        }
        break;
      case 'F':                                                    //  'F' moves
        switch(cmd[i+1])  {
          case '2':
            //Serial.print("F2 ");
            myCube.Fr2();
            break;
          case 39:
            //Serial.print("F' ");
            myCube.Frp();
            break;
          default:
            //Serial.print("F ");
            myCube.Fr();
            break;
        }
        break;
      case 'B':                                                    //  'B' moves
        switch(cmd[i+1])  {
          case '2':
            //Serial.print("B2 ");
            myCube.B2();
            break;
          case 39:
            //Serial.print("B' ");
            myCube.Bp();
            break;
          default:
            //Serial.print("B ");
            myCube.B();
            break;
        }
        break;

      // Scan commands  -----------------------------------------------------------
      case 'f':                                             // Scan Front side
        myCube.scanFront();
        //Serial.print("OKf ");
        break;
      case 'r':                                            // Scan Right side
        myCube.scanRight();
        //Serial.print("OKr");
        break;
      case 'b':                                            // Scan Back side
        myCube.scanBack();
        //Serial.print("OKb");
        break;
      case 'l':                                            // Scan Right side
        myCube.scanLeft();
        //Serial.print("OKl");
        break;
      case 'u':                                            // Scan Up side
        myCube.scanUp();
        //Serial.print("OKu");
        break;
      case 'd':                                            // Scan Down side
        myCube.scanDown();
        //Serial.print("OKd");
        break;
      case 'g':                                           // back to Front side
        myCube.scanFront2();
        //Serial.print("OKg");
        break;

      // Other commands  --------------------------------------------------------------
      case 'T':                                          // release gripper pressure
        myCube.seize();
        bip(40, 2);
        //if (DEBUG_SERIAL)    Serial.print("seize");
        break;
      case 'S':                                         // change move speed
        switch(cmd[i+1])  {
          case '2':
            myCube.setSpeed(HI_SPEED);
            //if (DEBUG_SERIAL)    Serial.print("High Speed");
            break;
          case '1':
            myCube.setSpeed(LOW_SPEED);
            //if (DEBUG_SERIAL)    Serial.print("Low Speed");
            break;
        }
        break;
      case 'V':                                         // bips
        switch(cmd[i+1])  {
          case '4':
            bip(80, 4);
            //if (DEBUG_SERIAL)    Serial.print("bip (4)");
            break;
          case '2':
            bip(80, 2);
            //if (DEBUG_SERIAL)    Serial.print("bip (2)");
            break;
          default:
            bip(80, 1);
            //if (DEBUG_SERIAL)    Serial.print("bip ");
            break;
        }
        break;

      default:
          break;
      }
     i++;
  }
  //if (DEBUG_SERIAL)    Serial.println();
  //bip(20, 2);
}

void bip(int duration, int n)    {            // Bip piezo: duration in ms, n repeats
  for(int i=0; i<n; i++)  {  
     digitalWrite(bipPin, HIGH);        
     delay(duration);
     digitalWrite(bipPin, LOW);         
     delay(75);
  }
}
