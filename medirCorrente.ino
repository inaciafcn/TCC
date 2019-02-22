#include "EmonLib.h"
 
EnergyMonitor SCT013;
 
int pinSCT = A2;   //Pino analógico conectado ao SCT-013
 

 
void setup()
{
    SCT013.current(pinSCT, 6.0606);
 
    Serial.begin(9600);
}
 
void loop()
{
   double Irms = SCT013.calcIrms(1480);   // Calcula o valor da Corrente
    Serial.println(Irms);
    delay(500);
}
