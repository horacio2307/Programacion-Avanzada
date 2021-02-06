global activo,contraseña

class Alarma:
    def __init__(self):
        pass
    def inicio(self,opcion):
        if(opcion==0):
                print("Alarma off\n")                
        else:
                global contraseña
                contraseña=input("Ingrese la contraseña\n")
                if(contraseña=="5555"):
                    print("Contraseña Correcta")
                    global activo
                    activo=1
                else:
                    activo=0
                    print("Contraseña incorrecta, la alarma se apagara\nAlarma off\n")
    def leer(self,sensor):
        global activo
        if(activo==1):
                    if(sensor!=0):
                        print("Se ha detectado una amenaza\n")
#    def para(self,opcion):
#
 #       global contraseña
 #       if(activo==1):
  #              while(opcion==1):
   #                     contraseña=input("Ingrese su contraseña para detener\n")
    #                    if(contraseña=="5555"):
     #                       print("Contraseña correcta\nAlarma off\n")
      #                  else:
       #                     contraseña=input("Intente otra vez")

sensor=0
activo=0
prueba=Alarma()
opcion=int(input("Desea activar la alarma?\n0-->No\nOtro-->Si\n"))
prueba.inicio(opcion)
if(activo==1):
    while(sensor==0):
            sensor=int(input("El sensor detecta?\n0-->No\nOtro-->Si\n"))
            prueba.leer(sensor)
   # opcion=input("Desea detener la alarma?\n1-->Si\nOtro-->No\n")
#prueba.para(opcion)
