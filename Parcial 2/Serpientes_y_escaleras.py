from tkinter import*
from random import*
import time

global dado, j1, j2, turno, numero_turno, ancho, largo

ancho = largo = 267

dado = turno = j1 = j2 = numero_turno = 0

def dados():

    global dado

    dado = randint(1,6)
    
    mostrar_dado()

    Avanza()

    gana()

    mostrar_posicion()

    posicion_print()

def mostrar_dado():

    global dado
    v_dado=Label(ventana,text="Valor dado :")
    v_dado.grid(column=2,row=1)
    v_dado2=Label(ventana,text=dado)
    v_dado2.grid(column=3,row=1)

def Avanza():

    global j1, j2, dado, turno, numero_turno

    a=""
    tiro=Label(ventana,text=a)
    tiro.grid(column=1,row=2)
    if (turno == 0):
        a="Turno jugador 1"
        tiro=Label(ventana,text=a)
        tiro.grid(column=1,row=2)
        j1 = j1 + dado
        turno = 1
    else:
        a="Turno jugador 2"
        tiro=Label(ventana,text=a)
        tiro.grid(column=1,row=2)
        j2 = j2 + dado
        turno = 0
    numero_turno=numero_turno+1
    Label(ventana,text="Dado tirado:").grid(column=2,row=2)
    Label(ventana,text=numero_turno).grid(column=3,row=2)

def mostrar_posicion():

    global j1, j2
    
    Label(ventana,text="Player 1 :").grid(column=4,row=1)
    Label(ventana,text=j1).grid(column=6,row=1)

    Label(ventana,text="Player 2 :").grid(column=4,row=2)
    Label(ventana,text=j2).grid(column=6,row=2)

def gana():

    global j1, j2

    j1=condiciones(j1)
    j2=condiciones(j2)
    if(j1>100):

        j1=200-j1

    if(j2>100):

        j2=200-j2

    if (j1==100):

        mensaje="Gana jugador 1"
        Label(ventana,text=mensaje,bg="Blue").grid(column=1,row=3)
        B1.config(state=DISABLED)


    elif(j2==100):

        mensaje="Gana jugador 2"
        Label(ventana,text=mensaje,bg="Blue").grid(column=1,row=3)
        B1.config(state=DISABLED)
        
def condiciones(a):

    x=a

    if(x==3):
        x=60

    if(x==6):
        x=47

    if(x==32):
        x=53

    if(x==45):
        x=86

    if(x==51):
        x=94

    if(x==61):
        x=83

    if(x==98):
        x=36

    if(x==93):
        x=43

    if(x==81):
        x=16

    if(x==68):
        x=55

    if(x==50):
        x=13

    return x

def posicion_print():

    global j1, j2  
    x1=int(j1%10)
    y1=int((j1-x1)/10)
    x2=int(j2%10)
    y2=int((j2-x2)/10)

    fila1=50*(9-y1)+25
    fila2=50*(9-y2)+25

    if(y1%2==0):
        columna1=50*(x1-1)+25
    else:
        columna1=50*(9-x1)+25+50

    if(y2%2==0):
        columna2=50*(x2-1)+25
    else:
        columna2=50*(9-x2)+25+50

    if(j1%10==0):

        if(y1%2==0):
            columna1=columna1+50
        else:
            columna1=columna1-50

        fila1=fila1+50

    if(j2%10==0):
        if(y2%2==0):
            columna2=columna2+50
        else:
            columna2=columna2-50
        fila2=fila2+50

    bj1.place(x=columna1,y=fila1)
    bj2.place(x=columna2,y=fila2)



ventana = Tk()
ventana.geometry("1000x1000")

i=PhotoImage(file="serpientesYescaleras.gif")
Label(ventana,image=i).grid(column=0,row=0)

B1=Button(ventana,text="Tirar dado",command=dados)
B1.grid(column=1,row=1)

bj1=Button(ventana,text="j1",bg="Green")
bj2=Button(ventana,text="j2",bg="Blue")


ventana.mainloop()
