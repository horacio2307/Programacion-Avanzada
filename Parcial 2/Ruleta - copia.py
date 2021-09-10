from tkinter import*
from random import*
global monto_jugador, aux, aumento, apuesta, bandera, ruleta

bandera=False
monto_jugador=aux=aumento=apuesta=ruleta=0

def activar_teclado():

    global aux
    aux=0
    b0.config(state=NORMAL)
    b1.config(state=NORMAL)
    b2.config(state=NORMAL)
    b3.config(state=NORMAL)
    b4.config(state=NORMAL)
    b5.config(state=NORMAL)
    b6.config(state=NORMAL)
    b7.config(state=NORMAL)
    b8.config(state=NORMAL)
    b9.config(state=NORMAL)

def bloquear_teclado():

    b0.config(state=DISABLED)
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def numero():

    global aux, aumento
    aux=aux*10+aumento

def aumento0():

    global aumento
    aumento = 0
    numero()

def aumento1():

    global aumento
    aumento = 1
    numero()

def aumento2():

    global aumento
    aumento = 2
    numero()

def aumento3():

    global aumento
    aumento = 3
    numero()

def aumento4():

    global aumento
    aumento = 4
    numero()

def aumento5():

    global aumento
    aumento = 5
    numero()

def aumento6():

    global aumento
    aumento = 6
    numero()

def aumento7():

    global aumento
    aumento = 7
    numero()

def aumento8():

    global aumento
    aumento = 8
    numero()

def aumento9():

    global aumento
    aumento = 9
    numero()

def ingresar_monto():

    global aux, apuesta, bandera
    bloquear_teclado()
    activar_teclado()

    apuesta=aux

    if(apuesta<500):

        bandera=FALSE

    else:
        bandera=TRUE

def ingresar_1ficha()

    Label(ventana,text="").grid(column=10,row=2)

def Jugar():

    global bandera, ruleta
    Label(ventana,text="").grid(column=10,row=1)
    if(bandera==TRUE):

        Label(ventana,text="Si puede jugar").grid(column=10,row=1)

        ruleta=randint(0,36)

    else():

        Label(ventana,text="No puede jugar").grid(column=10,row=1)



ventana=Tk()

b0=Button(ventana,text="0",command=aumento0)
b0.grid(column=0,row=1)

b1=Button(ventana,text="1",command=aumento1)
b1.grid(column=1,row=1)

b2=Button(ventana,text="2",command=aumento2)
b2.grid(column=2,row=1)

b3=Button(ventana,text="3",command=aumento3)
b3.grid(column=3,row=1)

b4=Button(ventana,text="4",command=aumento4)
b4.grid(column=4,row=1)

b5=Button(ventana,text="5",command=aumento5)
b5.grid(column=5,row=1)

b6=Button(ventana,text="6",command=aumento6)
b6.grid(column=6,row=1)

b7=Button(ventana,text="7",command=aumento7)
b7.grid(column=7,row=1)

b8=Button(ventana,text="8",command=aumento8)
b8.grid(column=8,row=1)

b9=Button(ventana,text="9",command=aumento9)
b9.grid(column=9,row=1)



ventana.mainloop()
