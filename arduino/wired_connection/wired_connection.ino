#include <CapacitiveSensorR4.h> // to use Arduino Uno R3, change this to Paul Bagder's Capacitive Sensing Library

CapacitiveSensor cs = CapacitiveSensor(6, 3);
void setup() {
  Serial.begin(115200); 
  // Serial.begin(9600); 
}

void loop() {
   //resistor should be pin 5 (start => in node)
  long sensorValue = cs.capacitiveSensor(30);
  Serial.println(sensorValue);
} 