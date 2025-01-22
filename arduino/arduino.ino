const int pinLed = 13;
const int pinSonido = 4;
const int frecuencia = 300;

char command = 'b';

void setup()
{
	pinMode(pinLed, OUTPUT);
  pinMode(pinSonido, OUTPUT);
	Serial.begin(9600);
}

void loop()
{
	if (Serial.available())
	{
		command = Serial.read();
	}

	if (command == 'a'){
    digitalWrite(pinLed, HIGH);
    tone(pinSonido, frecuencia);
  }
		
	if (command == 'b'){
    digitalWrite(pinLed, LOW);
    digitalWrite(pinSonido, LOW);
    noTone(pinSonido);

  }
		
}