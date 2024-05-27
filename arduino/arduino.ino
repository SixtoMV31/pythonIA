const int pinLed = 13;
const int pinSonido = 4;
const int frecuencia = 220;

char command = 'b';

void setup()
{
  Serial.begin(9600);
	pinMode(pinLed, OUTPUT);
  pinMode(pinSonido, OUTPUT);

}

void loop()
{
	if (Serial.available()){
		command = Serial.read();
	

	if (command == 'a'){
    digitalWrite(pinLed, HIGH);
    //digitalWrite(pinSonido, HIGH);
    tone(pinSonido, frecuencia);
    
    


  }
		
	if (command == 'b'){
    digitalWrite(pinLed, LOW);
    digitalWrite(pinSonido, LOW);
    noTone(pinSonido);
    

  }

  }
		
}