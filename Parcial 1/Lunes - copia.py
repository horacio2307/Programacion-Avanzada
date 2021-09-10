import time
class Lunes :

    def __init__ (self):
        pass

    def horario(self,hora):
        if (hora==7):
            print("Instrumentacion    Salon: 45\n")
        if (hora==8):
            print("Ingles    Salon: UAP9\n")
        if (hora==9):
            print("Microcrontoladores   Salon: 51\n")
        if (hora==10):
            print("Hora libre\n")
        if (hora==11):
            print("Dinamica de Sistemas  Salon: 51\n")
        if (hora==12):
            print("Hora libre\n")
        if (hora==13):
            print("Progra Avanzada  Salon: 14\n")
        if (hora==14):
            print("Progra Avanzada  Salon: 14\n")
        if(hora<=6 or hora >= 15):
            print("No es hora de clases :((\n")

