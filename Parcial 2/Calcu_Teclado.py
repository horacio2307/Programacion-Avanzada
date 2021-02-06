from tkinter import*

global Digito_1
global Digito_2
global auxiliar
global aumento
global bandera
global a


Acumulador=Digito_1=Digito_2=auxiliar=aumento=bandera=a=0

def numero():

    global Digito_1
    global aumento
    global bandera
    global Digito_2

    if(bandera==0):

        Digito_1 = Digito_1*10 + aumento
        #if(Digito_1>0):
        L_num=Label(ventana,text=Digito_1)
        L_num.grid(column=12,row=1)

    else:

        Digito_2 = Digito_2*10 +aumento
        #if (Digito_2>0):    
        L_num2=Label(ventana,text=Digito_2)
        L_num2.grid(column=18,row=1)


 
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

def suma():

    global bandera 

    bandera = 1

def resta():

    global bandera

    bandera = 2

def mult():

    global bandera
 
    bandera = 3
 
def div():

    global bandera
 
    bandera = 4
        
def resultado():

    global bandera
    global Digito_1
    global Digito_2
    global a

    if(bandera==1):
       # L_num=Label(ventana,text="La suma es :")
       # L_num.grid(column=0,row=5)
        a = Digito_1 + Digito_2
        L_num2=Label(ventana,text=a)
        L_num2.grid(column=4,row=5)

    if(bandera==2):
       # L_num=Label(ventana,text="La resta es :")
       # L_num.grid(column=0,row=5)
        a = Digito_1 - Digito_2
        L_num3=Label(ventana,text=a)
        L_num3.grid(column=4,row=5)

    if(bandera==3):
        #L_num=Label(ventana,text="La Multiplicacion es :")
        #L_num.grid(column=0,row=5)
        a = Digito_1 * Digito_2
        L_num4=Label(ventana,text=a)
        L_num4.grid(column=4,row=5)

    if(bandera==4):
        
        try:
            a=Digito_1/Digito_2
         #   L_num=Label(ventana,text="La division es :")
         #   L_num.grid(column=0,row=5)

        except ZeroDivisionError:
            a="Error de division"
            L_num5=Label(ventana,text=a)
            L_num5.grid(column=4,row=5)

    bandera=0
    Digito_1=0
    Digito_2=0
    
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("300x200")

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

b_suma=Button(ventana,text="+",command=suma)
b_suma.grid(column=0,row=2)

b_resta=Button(ventana,text="-",command=resta)
b_resta.grid(column=1,row=2)

b_multi=Button(ventana,text="*",command=mult)
b_multi.grid(column=2,row=2)

b_div=Button(ventana,text="/",command=div)
b_div.grid(column=3,row=2)

b_igual=Button(ventana,text="=",command=resultado)
b_igual.grid(column=4,row=2)


ventana.mainloop()