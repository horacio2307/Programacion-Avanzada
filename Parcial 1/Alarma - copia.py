global duracion
import time

class alarma:

    def __init__ (self,tiempo):

        self.tiempo=tiempo


    def conversion (self):

         global duracion

         duracion=self.tiempo*60
        
    def conteo (self):

        global duracion

        while (duracion>0): #Mientras que el tiempo sea mayor que cero resta un segundo

                time.sleep(0.1)
                duracion=duracion-1
                print ("Restan :",duracion, " segundos")

        if(duracion==0):

                duracion=0

                print ("Alarma activa")


minutos = float(input("Ingrese en cuantos minutos quiere que suene su alarma\n"))

prueba=alarma(minutos)

prueba.conversion()

prueba.conteo()



