const int pinLED = 13;
const int pinSonido = 4;
const int frecuencia = 500;

void setup() 
{
  Serial.begin(9600);
  pinMode(pinLED, OUTPUT);
  pinMode(pinSonido, OUTPUT);
}
void loop()
{
    char option = Serial.read();
    if (option == 'a')
      {
        digitalWrite(pinLED, HIGH);
        tone(pinSonido, frecuencia);
        delay(200);
      }
    if (option == 'b')
      {
        digitalWrite(pinLED, LOW);
        noTone(pinSonido);
        delay(200);
      }
  
}
