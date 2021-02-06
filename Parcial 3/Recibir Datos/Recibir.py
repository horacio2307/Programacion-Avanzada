import serial
import time 

arduino=serial.Serial('COM4',9600)
time.sleep(2)
i=1
while (i>0):
        dato=input("s --> On \nn --> Off\nx --> Salir")
        time.sleep(1)
        arduino.write(dato.encode())
        if (dato=='x'):
            i=0


arduino.close()
