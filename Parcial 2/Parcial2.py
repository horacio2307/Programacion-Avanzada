from tkinter import*
from random import*

global bandera, sigue, jugador, aux, monto_apuesta, sv

jugador=aux=monto_apuesta=0
bandera=sigue=TRUE

ancho=12
alto=2

def monto_inicial():

    global jugador

    jugador=int(input("Ingrese su monto inicial: "))

    Label(ventana,text="Monto inicial : ").grid(column=5,row=1)
    Label(ventana,text=jugador).grid(column=6,row=1)

    B1.config(state=DISABLED)
    B2.config(state=NORMAL)
    B3.config(state=NORMAL)
    B5.config(state=NORMAL)


def monto():

    global monto_apuesta, bandera

    monto_apuesta=int(input("Ingrese el monto a apostar :"))    
    
    B2.config(state=DISABLED)
    B6.config(state=NORMAL)

    Label(ventana,text="Apuesta :").grid(column=5,row=3)
    Label(ventana,text=monto_apuesta).grid(column=6,row=3)

    B8.config(NORMAL)    

def monto_total():

    global jugador, monto_apuesta

    monto_apuesta= jugador

    Label(ventana,text="Apuesta :").grid(column=5,row=3)
    Label(ventana,text=monto_apuesta).grid(column=6,row=3)

    B3.config(state=DISABLED)
    B6.config(state=DISABLED)
    B8.config(NORMAL)

def continua():

    global sigue
    sigue=TRUE

    Label(ventana,text="Su saldo es :").grid(column=5,row=2)
    Label(ventana,text=jugador).grid(column=6,row=2)

def retira():

    global sigue
    sigue=FALSE

    bloqueo()

def bloqueo():

    B1.config(state=DISABLED)
    B2.config(state=DISABLED)
    B3.config(state=DISABLED)
    B4.config(state=DISABLED)
    B5.config(state=DISABLED)
    B6.config(state=DISABLED)
    B7.config(state=DISABLED)
    B8.config(state=DISABLED)

def aumenta_apuesta():

    global aux, monto_apuesta 

    aux=int(input("Ingrese el aumento en la apuesta: "))

    monto_apuesta=monto_apuesta+aux

    Label(ventana,text="Apuesta :").grid(column=5,row=3)
    Label(ventana,text=monto_apuesta).grid(column=6,row=3)
    B8.config(NORMAL)

def Dividir():
    pass

def Apostar():
    pass

def rojo():
    pass

def negro():
    pass

def numero():
    pass

ventana=Tk()
ventana.geometry("750x800")

Label(ventana,text="Apuesta :").grid(column=5,row=3)
Label(ventana,text=monto_apuesta).grid(column=6,row=3)
B1=Button(ventana,text="Monto incial",command=monto_inicial,height=alto,width=ancho)
B1.grid(column=1,row=1)
B2=Button(ventana,text="Monto a apostar",command=monto,height=alto,width=ancho)
B2.grid(column=2,row=1)
B3=Button(ventana,text="Apuesta todo",command=monto_total,height=alto,width=ancho)
B3.grid(column=3,row=1)
B4=Button(ventana,text="Seguir",command=continua,height=alto,width=ancho)
B4.grid(column=1,row=2)
B5=Button(ventana,text="Retirarse",command=retira,height=alto,width=ancho)
B5.grid(column=2,row=2)
B6=Button(ventana,text="Subir apuesta",command=aumenta_apuesta,height=alto,width=ancho)
B6.grid(column=3,row=2)
B7=Button(ventana,text="Apuesta dividida",command=Dividir,height=alto,width=ancho)
B7.grid(column=1,row=3)
B8=Button(ventana,text="Apostar",command=Apostar,height=alto,width=ancho)
B8.grid(column=3,row=3)

Label(ventana,text="Su saldo es :").grid(column=5,row=2)
Label(ventana,text=jugador).grid(column=6,row=2)

bloqueo()

B1.config(state=NORMAL)
B5.config(state=NORMAL)

ventana.mainloop()