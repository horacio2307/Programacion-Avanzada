global c
global m
global g
global t

c=0
m=0
g=0
t=0

class clase:
    
    def __init__(self):

        pass

    def ingreso(self):

        global t

        t=t+1

        menu = """
        
        Tamaño Caja :

        0 -->   Chica
        1 -->   Mediana
        3 -->    Grande

        Si ingresa otro valor se considera caja grande

        """

        opcion = input(menu)

        if (opcion == "0"):

            global c

            c=c+1

        elif (opcion == "1"):

            global m

            m=m+1

        else :

            global g

            g=g+1

    def showT(self):

        global t

        print("\nSe han ingresado :",t," cajas totales\n")

    def show(self):

        global c
        global m
        global g

        print("\nSe han ingresado :",c," cajas chicas\n")
        print("\nSe han ingresado :",m," cajas medianas\n")
        print("\nSe han ingresado :",g," cajas grandes\n")

    def end(self):

            print("\nSe ingresaron :",t," cajas en total\n")
            print("\n",c," cajas chicas\n")
            print("\n",m," cajas medianas\n")
            print("\n",g," cajas grandes\n")

banda=clase()

flag =True


while (flag == True):

        b=input("\n¿Desea ingresar una caja?\nSi --> 1 \nNo --> Otro\n")

        if(b=="1"):

            flag2 = True

        else :

            flag2 = False

        while (flag2 == True):
            

                    banda.ingreso()

                    banda.showT()

                    ver=input("\n¿Desea ver distribuicion de los tamaños de cajas hasta ahora?\nSi --> 1 \nNo --> Otro\n")

                    if(ver=="1"):

                        banda.show()

                    again=input("\n¿Desea ingresar mas cajas?\nSi --> 1 \nNo --> Otro\n")

                    if(again=="1"):

                        flag2 = True

                    else :

                        flag = False 

                        flag2 = False

print("\nProceso terminado\n")

a=input("\n¿Desea ver la distribucion de las cajas?\nSi --> 1 \nNo --> Otro\n")

if(a=="1"):

    banda.end()

print("\nGracias!")

