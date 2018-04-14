int sensorPin = A0;    

int sensorValue = 0;  

void setup() {
  
  Serial.begin (9600);
}

void loop() {
  
  sensorValue = analogRead(sensorPin);
  //Serial.println(sensorValue);
  if(sensorValue>920)
  {delay(50);
    Serial.println("play");
    }
   else
    {delay(50);
    Serial.println("pause");
     }
 
}
