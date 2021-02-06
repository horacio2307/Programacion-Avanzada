class Martes :
    
    def __init__(self):
        pass

    def horario(self, hora):
        if (hora==7 or hora==8):
            print("Ingles   Salon: UAP9\n")
        
        if (hora==9 or hora==10):
            print("Competencias Directias   Salon: 51\n")

        if (hora==11 or hora==12):
            print("Analisis de fluidos  Salon: 41\n")

        if (hora==13 or hora==14):
            print("Progra Avanzada  Salon: 41\n")

        if(hora<=6 or hora>=15):
            print("No es hora de clase :((\n")
