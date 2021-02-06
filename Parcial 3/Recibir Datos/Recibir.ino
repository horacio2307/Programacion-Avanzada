#define led 13

void setup()
{
    Serial.begin(9600);
    pinMode(led, OUTPUT);
}

void loop()
{
    if (Serial.available()>0){

        char opcion = Serial.read();

        if(opcion=='s')

        digitalWrite(led, 1);

        else
        {
            digitalWrite(led, 0);
        }
        

    }
    
}
