#define Patio 3
#define Casa  4
#define Zotano 5

#define Led_P 8
#define Led_C 9
#define Led_Z 10

int Sensor_C, Sensor_P, Sensor_Z;

void setup()
{

    pinMode(Led_P, OUTPUT);
    pinMode(Led_C, OUTPUT);
    pinMode(Led_Z, OUTPUT);
    
    Serial.begin(9600);
}

void loop()
{


 if(Serial.available()>0){

     char dato=Serial.read();

     switch (dato) {
         case 'p':
           digitalWrite(Led_P, 1); delay(500);      digitalWrite(Led_P,0);
           break;
         case 'c':
           digitalWrite(Led_C, 1); delay(500);      digitalWrite(Led_C,0);
           break;
        case 'z':
        digitalWrite(Led_Z, 1); delay(500);         digitalWrite(Led_Z,0);
         default:
         
                  Sensor_C = digitalRead(Casa);
                  Sensor_P = digitalRead(Patio);
                  Sensor_Z = digitalRead(Zotano);
                  if(Sensor_C==1 || Sensor_P==1 || Sensor_Z==1){
                        digitalWrite(Led_C,1);
                        digitalWrite(Led_P,1);
                        digitalWrite(Led_Z,1);

                        delay(1000);

                        digitalWrite(Led_C,0);
                        digitalWrite(Led_P,0);
                        digitalWrite(Led_Z,0);
                  }


           break;
     }


     
     

 }


}
