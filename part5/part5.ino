#define pin8 8
#define pin9 9
#define pin10 10
#define pin11 11
#define pin4 4
#define pin5 5
#define pin6 6
#define pin7 7

void setup(){
  Serial.begin(9600);
  Serial.flush(); 
  pinMode(pin8, OUTPUT);
  pinMode(pin9, OUTPUT);
  pinMode(pin10, OUTPUT);
  pinMode(pin11, OUTPUT);
  pinMode(pin4, INPUT);
  pinMode(pin5, INPUT);
  pinMode(pin6, INPUT);
  pinMode(pin7, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop(){
  int pin4_value,pin5_value,pin6_value,pin7_value;
  String address_byte,data_byte;
  int address_byte_int,data_byte_int;
  if (Serial.available())  {
    address_byte = Serial.readStringUntil(',');
    data_byte = Serial.readStringUntil(',');
    address_byte_int = address_byte.toInt();
    data_byte_int = data_byte.toInt();
    switch(address_byte_int){
      case 0: digitalWrite(pin8,data_byte_int);
              pin4_value = digitalRead(pin4);
              Serial.print(pin4_value);
              for(int i=0;i<3;i++){
                digitalWrite(LED_BUILTIN, 1);
                delay(500);
                digitalWrite(LED_BUILTIN, 0);
                delay(500);
              }
              break;
      case 1: digitalWrite(pin9,data_byte_int);
              pin5_value = digitalRead(pin5);
              Serial.print(pin5_value); 
              break;
      case 2: digitalWrite(pin10,data_byte_int);
              pin6_value = digitalRead(pin6);
              Serial.print(pin6_value);
              break;
      case 3: digitalWrite(pin11,data_byte_int);
              pin7_value = digitalRead(pin7);
              Serial.print(pin7_value);
              break;
      case 4: int analogPIN_0_value = analogRead(A0),
              analogPIN_1_value = analogRead(A1),
              analogPIN_2_value = analogRead(A2),
              analogPIN_3_value = analogRead(A3);
              float analogPIN_0_voltage = analogPIN_0_value *(5.0/1023.0),
              analogPIN_1_voltage = analogPIN_1_value *(5.0/1023.0),
              analogPIN_2_voltage = analogPIN_2_value *(5.0/1023.0),
              analogPIN_3_voltage = analogPIN_3_value *(5.0/1023.0);
              Serial.print("4,");
              Serial.print(String(analogPIN_0_voltage));
              Serial.print(",");
              Serial.print("5,");
              Serial.print(String(analogPIN_1_voltage));
              Serial.print(",");
              Serial.print("6,");
              Serial.print(String(analogPIN_2_voltage));
              Serial.print(",");
              Serial.print("7,");
              Serial.print(String(analogPIN_3_voltage));
              Serial.print(",");
              break;
      }
    }
delay(10);
}
