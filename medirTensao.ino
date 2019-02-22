
const int voltageSensor = A0;

float vOUT = 0.0;
float tensao = 0.0;
float R1 = 30000.0;
float R2 = 7500.0;
int value = 0;

 
void setup()
{
   
 
    Serial.begin(9600);
}
 
void loop(){
   value = analogRead(voltageSensor);
   vOUT = (value * 5.0) / 1024.0;
   tensao = vOUT / (R2/(R1+R2));
    Serial.println(tensao);
    delay(500);
}
