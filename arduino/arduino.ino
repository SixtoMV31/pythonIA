const int pinLed = 13;

char command = 'b';

void setup()
{
	pinMode(pinLed, OUTPUT);
	Serial.begin(9600);
}

void loop()
{
	if (Serial.available())
	{
		command = Serial.read();
	}

	if (command == 'a')
		digitalWrite(pinLed, HIGH);
	if (command == 'b')
		digitalWrite(pinLed, LOW);
}