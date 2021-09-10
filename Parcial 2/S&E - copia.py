from tkinter import*
from random import*
import time

global dado, j1, j2, turno, numero_turno

dado = turno = j1 = j2 = numero_turno = 0

def dados():

    global dado

    dado = randint(1,6)
    
    mostrar_dado()

    Avanza()

    gana()

    mostrar_posicion()


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

    if(x==11):
        x=39

    if(x==17):
        x=67
    
    if(x==19):
        x=45

    if(x==21):
        x=56

    if(x==26):
        x=50

    if(x==43):
        x=84
    
    if(x==52):
        x=76

    if(x==70):
        x=92
    
    if(x==74):
        x=100

    if(x==96):
        x=69
    
    if(x==93):
        x=40

    if(x==83):
        x=8

    if(x==78):
        x=49
    
    if(x==75):
        x=30

    if(x==62):
        x=14

    if(x==36):
        x=20
    
    if(x==16):
        x=6
    
    if(x==22):
        x=2

    return x

    
ventana = Tk()
ventana.geometry("650x450")

i=PhotoImage(file="ser_&_esc.gif")
Label(ventana,image=i).grid(column=1,row=4)

B1=Button(ventana,text="Tirar dado",command=dados)
B1.grid(column=1,row=1)

ventana.mainloop()








