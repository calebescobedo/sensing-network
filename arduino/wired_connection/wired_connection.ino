#include <CapacitiveSensorR4.h> // to use Arduino Uno R3, change this to Paul Bagder's Capacitive Sensing Library

CapacitiveSensor cs_5_2 = CapacitiveSensor(5,2);        // 10M resistor between pins 4 & 2, pin 2 is sensor pin, add a wire and or foil if desired

void setup()                    
{
   cs_5_2.set_CS_AutocaL_Millis(0xFFFFFFFF);     // turn off autocalibrate on channel 1 - just as an example
   Serial.begin(9600);
   while (!Serial){
    ; 
   }
}

void loop()                    
{
    long total =  cs_5_2.capacitiveSensor(30);
    long time = millis();
    
    char buffer[50];
    sprintf(buffer, "%lu %lu\n", total, time);
    Serial.print(buffer);

    delay(20);                             // arbitrary delay to limit data to serial port 
}