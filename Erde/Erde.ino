/*
 *
 *
 *
 *
 *
 *
 *
 *
*/
//change this 4 pins to target pin aka pina
#define PIN_LED1 7
#define PIN_LED2 8
#define PIN_LED3 9
#define PIN_LED4 10

//long period = 1000;  //default blink period
int sensorValue;

class Blinker {
  private:
    byte pinLED;
    boolean ledState = LOW;
    unsigned long timeLedOn;
    unsigned long timeLedOff;
    unsigned long nextChangeTime = 0;

  public:
    Blinker(byte pinLED, unsigned long timeLedOn, unsigned long timeLedOff) {
      this->pinLED = pinLED;
      this->timeLedOn = timeLedOn;
      this->timeLedOff = timeLedOff;
      // initialize digital pin LED as an output.
      pinMode(pinLED, OUTPUT);
    }

    // Checks whether it is time to turn on or off the LED.
    void check() {
      unsigned long currentTime = millis();

      if(currentTime >= nextChangeTime) {

        if(ledState) {
          // LED is currently turned On. Turn Off LED.
          ledState = LOW;
          nextChangeTime = currentTime + timeLedOff;
        }
        else{
          // LED is currently turned Off. Turn On LED.
          ledState = HIGH;
          nextChangeTime = currentTime + timeLedOn;
        }

        digitalWrite(pinLED, ledState);
      }
    }
    void update(unsigned long period){
      this->timeLedOn = period;
      this->timeLedOff = period;
    }
};

Blinker blink1 = Blinker(PIN_LED1, 1000, 1000);
Blinker blink2 = Blinker(PIN_LED2, 1000, 1000);
Blinker blink3 = Blinker(PIN_LED3, 1000, 1000);
Blinker blink4 = Blinker(PIN_LED4, 1000, 1000);

// the setup function runs once when you press reset or power the board
void setup() {
  // initalize serial
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  if (Serial.available()) {
    String message = Serial.readString(); // no need to string it readString() it
    int pina = message.substring(0, 2).toInt();
    if (pina = 1){
      blink1.update(message.substring(2).toInt());    //read, write, print
    }
    if (pina = 2){
      blink2.update(message.substring(2).toInt());    //read, write, print
    }
    if (pina = 3){
      blink3.update(message.substring(2).toInt());    //read, write, print
    }
    if (pina = 4){
      blink4.update(message.substring(2).toInt());    //read, write, print
    }
    //char input = Serial.read();
    //blink3.update(Serial.parseInt());    //read, write, print
    //Serial.print(period);   //to check if recieved
    //Serial.println(" recieved"); //debug
  }
  Serial.print(analogRead(5));
  Serial.print("/");
  Serial.print(analogRead(4));
  Serial.print("/");
  Serial.print(analogRead(3));
  Serial.print("/");
  Serial.print(analogRead(2));
  Serial.print("/");
  Serial.print(analogRead(1));
  Serial.print("/");
  Serial.print(analogRead(0));
  Serial.println();
  //Dirty check for all bliners
  blink1.check();
  blink2.check();
  blink3.check();
  blink4.check();
  //period = Serial.parseInt();    //read, write, print
  //Serial.println(period);           //debug
  //digitalWrite(9, HIGH);   // turn the LED on (HIGH is the voltage level)
  //delay(period);                       // wait for a second
  //digitalWrite(9, LOW);    // turn the LED off by making the voltage LOW
  //delay(period);                       // wait for a second
}

