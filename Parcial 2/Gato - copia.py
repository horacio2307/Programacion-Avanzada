from tkinter import*

global aux
global A1
global A2
global A3
global A4
global A5
global A6
global A7
global A8
global A9
global bandera
aux = 0
A1 = A2 = A3 = A4 = A5 = A6 = A7 = A8 = A9 = 10
bandera = 2

def resultado():

    global A1
    global A2
    global A3
    global A4
    global A5
    global A6
    global A7
    global A8
    global A9
    global bandera

    if (A1+A2+A3==0):

        bandera = 1

    if (A4+A5+A6==0):
        
        bandera = 1

    if (A7+A8+A9==0):

        bandera = 1

    if (A1+A4+A7==0):

        bandera = 1

    if (A2+A5+A8==0):

        bandera = 1

    if (A3+A6+A9==0):

        bandera = 1

    if (A1+A5+A9==0):

        bandera = 1

    if (A3+A5+A7==0):

        bandera = 1

    if (A1+A2+A3==3):

        bandera = 0

    if (A4+A5+A6==3):
        
        bandera = 0

    if (A7+A8+A9==3):

        bandera = 0

    if (A1+A4+A7==3):

        bandera = 0

    if (A2+A5+A8==3):

        bandera = 0

    if (A3+A6+A9==3):

        bandera = 0

    if (A1+A5+A9==3):

        bandera = 0

    if (A3+A5+A7==3):

        bandera = 0

    if (bandera == 0):
        
        print_won = Label(ventana,text="Gano 1")
        print_won.grid(column = 10 , row =  3)

    elif (bandera == 1):
        print_won = Label(ventana,text="Gano 0")
        print_won.grid(column = 10 , row =  3)

    else: 
        print_won = Label(ventana,text="Empate")
        print_won.grid(column = 10 , row =  3)


def Reinicio():

    global bandera
    global A1
    global A2
    global A3
    global A4
    global A5
    global A6
    global A7
    global A8
    global A9

    A1 = A2 = A3 = A4 = A5 = A6 = A7 = A8 = A9 = 10

    V1= Label(ventana,text="#")
    V2= Label(ventana,text="#")
    V3= Label(ventana,text="#")
    V4= Label(ventana,text="#")
    V5= Label(ventana,text="#")
    V6= Label(ventana,text="#")
    V7= Label(ventana,text="#")
    V8= Label(ventana,text="#")
    V9= Label(ventana,text="#")
    B1.config(state=NORMAL)
    B2.config(state=NORMAL)
    B3.config(state=NORMAL)
    B4.config(state=NORMAL)
    B5.config(state=NORMAL)
    B6.config(state=NORMAL)
    B7.config(state=NORMAL)
    B8.config(state=NORMAL)
    B9.config(state=NORMAL)
    V1.grid(column=0,row=0)
    V2.grid(column=1,row=0)
    V3.grid(column=2,row=0)
    V4.grid(column=0,row=1)
    V5.grid(column=1,row=1)
    V6.grid(column=2,row=1)
    V7.grid(column=0,row=2)
    V8.grid(column=1,row=2)
    V9.grid(column=2,row=2)
    bandera=2

#def uno():

#    global aux

#    aux = 1

#def cero():

#    global aux

#    aux = 0

def c1():

    global aux
    global A1

    A1 = aux

    V1 = Label(ventana,text=aux)
    V1.grid(column=0,row=0)
    B1.config(state=DISABLED)

    if(aux==0):

        aux = 1

    else:

        aux = 0

def c2():

    global aux
    global A2

    A2 = aux
    
    V2 = Label(ventana,text=aux)
    V2.grid(column=1,row=0)
    B2.config(state=DISABLED)

    if(aux==0):

        aux = 1

    else:

        aux = 0

def c3():

    global aux
    global A3

    A3 = aux
    
    V3 = Label(ventana,text=aux)
    V3.grid(column=2,row=0)
    B3.config(state=DISABLED)

    if(aux==0):

        aux = 1

    else:

        aux = 0

def c4():

    global aux
    global A4

    A4 = aux
    
    V4 = Label(ventana,text=aux)
    V4.grid(column=0,row=1)
    B4.config(state=DISABLED)

    if(aux==0):

        aux = 1

    else:

        aux = 0

def c5():

    global aux
    global A5

    A5 = aux
    
    V5 = Label(ventana,text=aux)
    V5.grid(column=1,row=1)
    B5.config(state=DISABLED)

    if(aux==0):

        aux = 1

    else:

        aux = 0

def c6():

    global aux
    global A6

    A6 = aux
    
    V6= Label(ventana,text=aux)
    V6.grid(column=2,row=1)
    B6.config(state=DISABLED)

    if(aux==0):

        aux = 1

    else:

        aux = 0

def c7():

    global aux
    global A7

    A7 = aux
    
    V7 = Label(ventana,text=aux)
    V7.grid(column=0,row=2)
    B7.config(state=DISABLED)

    if(aux==0):

        aux = 1

    else:

        aux = 0

def c8():

    global aux
    global A8

    A8 = aux
    
    V8 = Label(ventana,text=aux)
    V8.grid(column=1,row=2)
    B8.config(state=DISABLED)

    if(aux==0):

        aux = 1

    else:

        aux = 0

def c9():

    global aux
    global A9

    A9 = aux
    
    V9 = Label(ventana,text=aux)
    V9.grid(column=2,row=2)
    B9.config(state=DISABLED)

    if(aux==0):

        aux = 1

    else:

        aux = 0


ventana = Tk()

B1 = Button(ventana,text="1,1",command=c1)
B2 = Button(ventana,text="1,2",command=c2)
B3 = Button(ventana,text="1,3",command=c3) 
B4 = Button(ventana,text="2,1",command=c4)
B5 = Button(ventana,text="2,2",command=c5)
B6 = Button(ventana,text="2,3",command=c6)
B7 = Button(ventana,text="3,1",command=c7)
B8 = Button(ventana,text="3,2",command=c8)
B9 = Button(ventana,text="3,3",command=c9)
#B_0 = Button(ventana,text="0",command=cero)
#B_1 = Button(ventana,text="1",command=uno)
B_Rei = Button(ventana,text="Reiniciar juego",command=Reinicio)
V1= Label(ventana,text="#")
V2= Label(ventana,text="#")
V3= Label(ventana,text="#")
V4= Label(ventana,text="#")
V5= Label(ventana,text="#")
V6= Label(ventana,text="#")
V7= Label(ventana,text="#")
V8= Label(ventana,text="#")
V9= Label(ventana,text="#")
V1.grid(column=0,row=0)
V2.grid(column=1,row=0)
V3.grid(column=2,row=0)
V4.grid(column=0,row=1)
V5.grid(column=1,row=1)
V6.grid(column=2,row=1)
V7.grid(column=0,row=2)
V8.grid(column=1,row=2)
V9.grid(column=2,row=2)
B1.grid(column=3,row=0)
B2.grid(column=4,row=0)
B3.grid(column=5,row=0)
B4.grid(column=3,row=1)
B5.grid(column=4,row=1)
B6.grid(column=5,row=1)
B7.grid(column=3,row=2)
B8.grid(column=4,row=2)
B9.grid(column=5,row=2)
#B_0.grid(column=7,row=1)
#B_1.grid(column=7,row=2)
B_Rei.grid(column=8,row=1)

B_fin = Button(ventana,text="Ver resultado",command=resultado)
B_fin.grid(column=8,row=5)

ventana.mainloop()
