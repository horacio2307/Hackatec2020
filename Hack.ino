//Hijos de Abraham

int i=0;

void off(){

    for(i=2;i<7;i++)
    digitalWrite(i,0);
}

void setup() {
  // put your setup code here, to run once:
 DDRB = B00111111; //Pines [8-12] entradas el pin 13 sera la salida
 for(i=2;i<7;i++)
    pinMode(i,OUTPUT);
 PORTB = B11111111; //Activamos resistencias Pull-up
 Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

        if(digitalRead(8)==LOW){

             Serial.println('a');

             digitalWrite(2,1);
             
        }
      
        else if(digitalRead(9)==LOW){

             Serial.println('b');
             digitalWrite(3,1);
        }
        else if(digitalRead(10)==LOW){

          Serial.println('c');
          digitalWrite(4,1);
        }
           
        else if(digitalRead(11)==LOW){
          Serial.println('d');
          digitalWrite(5,1);
        }
      
        else if(digitalRead(12)==LOW){

          Serial.println('e');
          digitalWrite(6,1);
        }
         
        else if (digitalRead(13)==LOW){

          Serial.println('x');
          off();
        }

        delay(500);
}
