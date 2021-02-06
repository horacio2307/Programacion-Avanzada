from Lunes     import *
from Martes    import *
from Miercoles import *
from Jueves    import * 
from Viernes   import * 

#from Martes import *


menu="""
Escoja un dia
Lunes       1
Martes      2
Miercoles   3
Jueves      4
Viernes     5

"""

state = True  #Forzamos a entrar al ciclo
b=0           #Salida del ciclo

while( state == True ):

    opcion=int(input(menu))

    a=0           #Indicador de opcion valida

    if (opcion==1):
        horario=Lunes()
        a=1
    if (opcion==2):
        horario=Martes()
        a=1
    if (opcion==3):
        horario=Miercoles()
        a=1
    if (opcion==4):
        horario=Jueves()
        a=1
    if (opcion==5):
        horario=Viernes()
        a=1
    if (a==0):
        print("\nIngrese una opcion valida :(\n")
    
    else:
        
        hour=int(input("\nIngrese la hora que desea ver //24hrs//\n\n"))

        if (opcion==1):

            print("\nEl dia Lunes a la hora ",hour," usted tiene\n")

            horario.horario(hour)

        if (opcion==2):

            print("\nEl dia Martes a la hora ",hour," usted tiene\n")

            horario.horario(hour)

        if (opcion==3):

            print("\nEl dia Miercoles a la hora ",hour," usted tiene\n")

            horario.horario(hour)

        if (opcion==4):

            print("\nEl dia Jueves a la hora ",hour," usted tiene\n")

            horario.horario(hour)

        if (opcion==5):

            print("\nEl dia Viernes a la hora ",hour," usted tiene\n")

            horario.horario(hour)

        
        b=int(input("\nSi desea checar otra hora ingrese un 1\n\nSi desea salir ingrese otro numero\n\n"))
 
        if (b==1):
            state = True
        else:
            state = False

print("\nFue un placer ayudarle\n")