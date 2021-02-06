from tkinter import*
import time
from random import randint

global contador,casino,contador1, bot_esp,ficha,apuesta,ba1,ba2,ba3,ba4,ruleta,num_ruleta
contador=0
contador1=0
bot_esp=0
ficha=0
apuesta=0

def acu0():
    global contador
    contador=10*contador+0
    l=Label(ventana,text=contador,bg="cyan",fg="black",width=15,height=5).grid(column=1, row=0)

def acu1():
    global contador
    contador=10*contador+1
    l=Label(ventana,text=contador,bg="cyan",fg="black",width=15,height=5).grid(column=1, row=0)

def acu2():
    global contador
    contador=10*contador+2
    l=Label(ventana,text=contador,bg="cyan",fg="black",width=15,height=5).grid(column=1, row=0)

def acu3():
    global contador
    contador=10*contador+3
    l=Label(ventana,text=contador,bg="cyan",fg="black",width=15,height=5).grid(column=1, row=0)

def acu4():
    global contador
    contador=10*contador+4
    l=Label(ventana,text=contador,bg="cyan",fg="black",width=15,height=5).grid(column=1, row=0)

def acu5():
    global contador
    contador=10*contador+5
    l=Label(ventana,text=contador,bg="cyan",fg="black",width=15,height=5).grid(column=1, row=0)

def acu6():
    global contador
    contador=10*contador+6
    l=Label(ventana,text=contador,bg="cyan",fg="black",width=15,height=5).grid(column=1, row=0)

def acu7():
    global contador
    contador=10*contador+7
    l=Label(ventana,text=contador,bg="cyan",fg="black",width=15,height=5).grid(column=1, row=0)

def acu8():
    global contador
    contador=10*contador+8
    l=Label(ventana,text=contador,bg="cyan",fg="black",width=15,height=5).grid(column=1, row=0)

def acu9():
    global contador
    contador=10*contador+9
    l=Label(ventana,text=contador,bg="cyan",fg="black",width=15,height=5).grid(column=1, row=0)

def entrar():
    global contador,casino,contador1,ba2,ba3,ba1
    contador1=contador
    contador=0
    if(contador1>=500):
        casino=Toplevel()
        casino.geometry("900x300")
        tablero=PhotoImage(file="tablero.gif")
        l=Label(casino,image=tablero).place(x=0,y=0)
        l1=Label(casino,text=("dinero:",contador1),font="arial 18").place(x=650,y=0, height=50)
        ventana.withdraw()
        ba1=Button(casino,text="ficha",command=elegficha,bg="green",fg="black")
        ba1.place(x=605,y=150,width=70,height=50)
        ba2=Button(casino,text="girar",bg="silver",fg="black",state=DISABLED,command=girar)
        ba2.place(x=675,y=150,width=70,height=50)
        ba3=Button(casino,text="apostar",command=apostar,bg="gold",fg="black",state=DISABLED)
        ba3.place(x=745,y=150,width=70,height=50)
        ba4=Button(casino,text="salir",command=exit,bg="red",fg="white",)
        ba4.place(x=745,y=200,width=70,height=50)
        casino.mainloop()
    else:
        l2=Label(ventana,text="cantidad insuficiente",bg="green",fg="white",width=15,height=5).grid(column=1, row=0)

def elegficha():
    global contador,casino,contador1, bot_esp,ficha,apuesta,ba1,ba2,ba3,ruleta,num_ruleta
    contador=0
    bot_esp=0
    ficha=0
    apuesta=0
    num_ruleta=0
    ventana.deiconify()
    casino.withdraw()
    l=Label(ventana,text=contador,bg="cyan",fg="black",width=15,height=5).grid(column=1, row=0)
    l=Label(ventana,text="ficha",width=15,height=5).grid(column=0,row=0)
    l1=Label(ventana,text="ficha",width=15,height=5).grid(column=2,row=0)
    b10.config(text="1 to 18",bg="green",command=rang1)
    b11.config(state=NORMAL)
    b12.config(state=NORMAL)
    b13.config(state=NORMAL)
    b14.config(state=NORMAL)
    b15.config(state=NORMAL)
    b16.config(state=NORMAL)
    b17.config(state=NORMAL)
    b18.config(state=NORMAL)
    b19.config(state=NORMAL)
    b20.config(state=NORMAL)
    b21.config(state=NORMAL)
    b11.grid(column=0,row=4)
    b12.grid(column=0,row=5)
    b13.grid(column=1,row=5)
    b14.grid(column=2,row=5)
    b15.grid(column=0,row=6)
    b16.grid(column=1,row=6)
    b17.grid(column=2,row=6)
    b18.grid(column=3,row=2)
    b19.grid(column=3,row=3)
    b20.grid(column=3,row=4)
    b21.grid(column=3,row=5)
    b22.grid(column=3,row=1)
    
def rang1():
    global bot_esp
    bot_esp=1
    l=Label(ventana,bg="cyan",fg="black",width=15,height=5,text="1 to 18").grid(column=1, row=0)
    bloqueo()

def rang2():
    global bot_esp
    bot_esp=2
    l=Label(ventana,bg="cyan",fg="black",width=15,height=5,text="19 to 36").grid(column=1, row=0)
    bloqueo()

def rang3():
    global bot_esp
    bot_esp=3
    l=Label(ventana,bg="cyan",fg="black",width=15,height=5,text="1 to 12").grid(column=1, row=0)
    bloqueo()

def rang4():
    global bot_esp
    bot_esp=4
    l=Label(ventana,bg="cyan",fg="black",width=15,height=5,text="13 to 24").grid(column=1, row=0)
    bloqueo()

def rang5():
    global bot_esp
    bot_esp=5
    l=Label(ventana,bg="cyan",fg="black",width=15,height=5,text="25 to 36").grid(column=1, row=0)
    bloqueo()

def rang6():
    global bot_esp
    bot_esp=6
    l=Label(ventana,bg="cyan",fg="black",width=15,height=5,text="fila 1").grid(column=1, row=0)
    bloqueo()

def rang7():
    global bot_esp
    bot_esp=7
    l=Label(ventana,bg="cyan",fg="black",width=15,height=5,text="fila 2").grid(column=1, row=0)
    bloqueo()

def rang8():
    global bot_esp
    bot_esp=8
    l=Label(ventana,bg="cyan",fg="black",width=15,height=5,text="fila 3").grid(column=1, row=0)
    bloqueo()

def rang9():
    global bot_esp
    bot_esp=9
    l=Label(ventana,bg="cyan",fg="black",width=15,height=5,text="PAR").grid(column=1, row=0)
    bloqueo()

def rang10():
    global bot_esp
    bot_esp=10
    l=Label(ventana,bg="cyan",fg="black",width=15,height=5,text="IMPAR").grid(column=1, row=0)
    bloqueo()

def rang11():
    global bot_esp
    bot_esp=11
    l=Label(ventana,bg="cyan",fg="black",width=15,height=5,text="ROJOS").grid(column=1, row=0)
    bloqueo()

def rang12():
    global bot_esp
    bot_esp=12
    l=Label(ventana,bg="cyan",fg="black",width=15,height=5,text="NEGROS").grid(column=1, row=0)
    bloqueo()

def listo():
    global contador,bot_esp,ficha,ba3,ba1,casino
    ficha=contador
    contador=0
    if(ficha<=36 or bot_esp>0):
        ventana.withdraw()
        casino.deiconify()
        ba1.config(state=DISABLED)
        ba3.config(state=NORMAL)
        if(bot_esp==1):
            l2=Label(casino,text=(" fichas 1 to 18 (x2)"),font="arial 18").place(x=630,y=50, height=50)
        elif(bot_esp==2):
            l2=Label(casino,text=(" fichas 19 to 36 (x2)"),font="arial 18").place(x=630,y=50, height=50)
        elif(bot_esp==3):
            l2=Label(casino,text=(" fichas 1 to 12 (x3)"),font="arial 18").place(x=630,y=50, height=50)
        elif(bot_esp==4):
            l2=Label(casino,text=(" fichas 13 to 24 (x3)"),font="arial 18").place(x=630,y=50, height=50)
        elif(bot_esp==5):
            l2=Label(casino,text=(" fichas 25 to 36 (x3)"),font="arial 18").place(x=630,y=50, height=50)
        elif(bot_esp==6):
            l2=Label(casino,text=("fichas fila 1 (x3)"),font="arial 18").place(x=630,y=50, height=50)
        elif(bot_esp==7):
            l2=Label(casino,text=("fichas fila 2 (x3)"),font="arial 18").place(x=630,y=50, height=50)
        elif(bot_esp==8):
            l2=Label(casino,text=("fichas fila 3 (x3)"),font="arial 18").place(x=630,y=50, height=50)
        elif(bot_esp==9):
            l2=Label(casino,text=("fichas PAR (x2)"),font="arial 18").place(x=630,y=50, height=50)
        elif(bot_esp==10):
            l2=Label(casino,text=("fichas IMPAR (x2)"),font="arial 18").place(x=630,y=50, height=50)
        elif(bot_esp==11):
            l2=Label(casino,text=("fichas rojas (x2)"),font="arial 18").place(x=630,y=50, height=50)
        elif(bot_esp==12):
            l2=Label(casino,text=("fichas negras (x2)"),font="arial 18").place(x=630,y=50, height=50)
        else:
            l2=Label(casino,text=("ficha:",ficha,"(x4)"),font="arial 18").place(x=630,y=50, height=50)
    else:
        l2=Label(ventana,text="ficha no existe",bg="green",fg="white",width=15,height=5).grid(column=1, row=0)

def apostar():
    global contador,contador1,ba3
    if(contador1>=500):
        ventana.deiconify()
        casino.withdraw()
        l2= l=Label(ventana,text="",bg="cyan",fg="black",width=15,height=5).grid(column=1, row=0)
        l=Label(ventana,text="minimo $500",width=15,height=5).grid(column=0,row=0)
        l1=Label(ventana,text="minimo $500",width=15,height=5).grid(column=2,row=0)
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
        b10.config(text="entrar",bg="blue",fg="white",command=apuestas,state=NORMAL)
        b11.grid_forget()
        b12.grid_forget()
        b13.grid_forget()
        b14.grid_forget()
        b15.grid_forget()
        b16.grid_forget()
        b17.grid_forget()
        b18.grid_forget()
        b19.grid_forget()
        b20.grid_forget()
        b21.grid_forget()
        b22.grid_forget()
    else:
        ba3.config(text="no money",state=DISABLED)
        ba4=Button(casino,text="salir",command=exit,bg="red",fg="white",)
        ba4.place(x=745,y=200,width=70,height=50)

def exit():
    ventana.destroy()

def apuestas():
    global contador,apuesta,ba2,ba3,casino
    apuesta=contador
    contador=0
    if(apuesta>=500):
        ventana.withdraw()
        casino.deiconify()
        ba2.config(state=NORMAL)
        ba3.config(state=DISABLED)
        l3=Label(casino,text=("apuestas:",apuesta),font="arial 18").place(x=630,y=100, height=50)
    else:
        l2=Label(ventana,text="es muy poco",bg="cyan",fg="black",width=15,height=5).grid(column=1, row=0)   

def girar():
    global contador1, bot_esp,ficha,apuesta,ba1,ba2,ba3,ruleta,num_ruleta
    casino.withdraw()
    ruleta=Toplevel()
    ruleta.geometry("200x200")
    time.sleep(1)
    if(bot_esp==11 or bot_esp==12):
        num_ruleta=randint(1,2)
        if(num_ruleta==1):
            r=Label(ruleta,text="",bg="red")
            r.place(x=0,y=0,width=100,height=100)
            ganador()
        elif(num_ruleta==2):
            r=Label(ruleta,text="",bg="black")
            r.place(x=0,y=0,width=100,height=100)
            ganador()
    else:
        num_ruleta=randint(0,36)
        r=Label(ruleta,text=num_ruleta,bg="grey")
        r.place(x=0,y=0,width=100,height=100)
        ganador()
    
def ganador():
    global contador1, bot_esp,ficha,apuesta,ba1,ba2,ba3,ruleta,num_ruleta
    if(bot_esp==0):
        if(ficha==num_ruleta):
            contador1=contador1+(apuesta*4)
        else:
            contador1=contador1-apuesta
    elif(bot_esp==1):
        if(num_ruleta>=1 and num_ruleta<=18):
            contador1=contador1+(apuesta*2)
        else:
            contador1=contador1-apuesta
    elif(bot_esp==2):
        if(num_ruleta>=19 and num_ruleta<=36):
            contador1=contador1+(apuesta*2)
        else:
            contador1=contador1-apuesta
    elif(bot_esp==3):
        if(num_ruleta>=1 and num_ruleta<=12):
            contador1=contador1+(apuesta*3)
        else:
            contador1=contador1-apuesta
    elif(bot_esp==4):
        if(num_ruleta>=13 and num_ruleta<=24):
            contador1=contador1+(apuesta*3)
        else:
            contador1=contador1-apuesta
    elif(bot_esp==5):
        if(num_ruleta>=25 and num_ruleta<=36):
            contador1=contador1+(apuesta*3)
        else:
            contador1=contador1-apuesta
    elif(bot_esp==6):
        if(num_ruleta==1 or num_ruleta==4 or num_ruleta==7 or num_ruleta==10 or num_ruleta==13 or num_ruleta==16 or num_ruleta==19 or num_ruleta==22 or num_ruleta==25 or num_ruleta==28 or num_ruleta==31 or num_ruleta==34):
            contador1=contador1+(apuesta*3)
        else:
            contador1=contador1-apuesta
    elif(bot_esp==7):
        if(num_ruleta==2 or num_ruleta==5 or num_ruleta==8 or num_ruleta==11 or num_ruleta==14 or num_ruleta==17 or num_ruleta==20 or num_ruleta==23 or num_ruleta==26 or num_ruleta==29 or num_ruleta==32 or num_ruleta==35):
            contador1=contador1+(apuesta*3)
        else:
            contador1=contador1-apuesta
    elif(bot_esp==8):
        if(num_ruleta==3 or num_ruleta==6 or num_ruleta==9 or num_ruleta==12 or num_ruleta==15 or num_ruleta==18 or num_ruleta==21 or num_ruleta==24 or num_ruleta==27 or num_ruleta==30 or num_ruleta==33 or num_ruleta==36):
            contador1=contador1+(apuesta*3)
        else:
            contador1=contador1-apuesta
    elif(bot_esp==9):
        if(num_ruleta%2==0):
            contador1=contador1+(apuesta*2)
        else:
            contador1=contador1-apuesta
    elif(bot_esp==10):
        if(num_ruleta%2!=0):
            contador1=contador1+(apuesta*2)
        else:
            contador1=contador1-apuesta
    elif(bot_esp==11):
        if(num_ruleta==1):
           contador1=contador1+(apuesta*2)
        else:
            contador1=contador1-apuesta 
    elif(bot_esp==12):
        if(num_ruleta==2):
           contador1=contador1+(apuesta*2)
        else:
            contador1=contador1-apuesta 

    l1=Label(casino,text=("dinero:",contador1),font="arial 18").place(x=650,y=0, height=50)
    j1=Button(ruleta,text="continuar jugando",command=continuar,bg="gold",fg="black")
    j1.place(x=0,y=100,width=100,height=50)
    ba1.config(state=NORMAL)
    ba2.config(state=DISABLED)

def continuar():
    ruleta.withdraw()
    casino.deiconify()

def bloqueo():

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
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)
    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)
    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

ventana=Tk()
l=Label(ventana,text="Bienvenido al casino",width=15,height=5).grid(column=0,row=0)
l1=Label(ventana,text="ingrese cantidad",width=15,height=5).grid(column=2,row=0)
l2=Label(ventana,text="",bg="cyan",fg="black",width=15,height=5).grid(column=1, row=0)
b0=Button(ventana,text="0",command=acu0,bg="blue",fg="white",width=15,height=5)
b0.grid(column=1,row=4)
b1=Button(ventana,text="1",command=acu1,bg="blue",fg="white",width=15,height=5)
b1.grid(column=0,row=3)
b2=Button(ventana,text="2",command=acu2,bg="blue",fg="white",width=15,height=5)
b2.grid(column=1,row=3)
b3=Button(ventana,text="3",command=acu3,bg="blue",fg="white",width=15,height=5)
b3.grid(column=2,row=3)
b4=Button(ventana,text="4",command=acu4,bg="blue",fg="white",width=15,height=5)
b4.grid(column=0,row=2)
b5=Button(ventana,text="5",command=acu5,bg="blue",fg="white",width=15,height=5)
b5.grid(column=1,row=2)
b6=Button(ventana,text="6",command=acu6,bg="blue",fg="white",width=15,height=5)
b6.grid(column=2,row=2)
b7=Button(ventana,text="7",command=acu7,bg="blue",fg="white",width=15,height=5)
b7.grid(column=0,row=1)
b8=Button(ventana,text="8",command=acu8,bg="blue",fg="white",width=15,height=5)
b8.grid(column=1,row=1)
b9=Button(ventana,text="9",command=acu9,bg="blue",fg="white",width=15,height=5)
b9.grid(column=2,row=1)
b10=Button(ventana,text="entrar",command=entrar,bg="blue",fg="white",width=15,height=5)
b10.grid(column=2,row=4)
b11=Button(ventana,text="19 to 36",bg="green",fg="white",width=15,height=5,command=rang2)
b11.grid(column=0,row=4)
b12=Button(ventana,text="1 to 12",bg="green",fg="white",width=15,height=5,command=rang3)
b12.grid(column=0,row=5)
b13=Button(ventana,text="13 to 24",bg="green",fg="white",width=15,height=5,command=rang4)
b13.grid(column=1,row=5)
b14=Button(ventana,text="25 to 36",bg="green",fg="white",width=15,height=5,command=rang5)
b14.grid(column=2,row=5)
b15=Button(ventana,text="fila 1",bg="green",fg="white",width=15,height=5,command=rang6)
b15.grid(column=0,row=6)
b16=Button(ventana,text="fila 2",bg="green",fg="white",width=15,height=5,command=rang7)
b16.grid(column=1,row=6)
b17=Button(ventana,text="fila 3",bg="green",fg="white",width=15,height=5,command=rang8)
b17.grid(column=2,row=6)
b18=Button(ventana,text="PAR",bg="green",fg="white",width=15,height=5,command=rang9)
b18.grid(column=3,row=2)
b19=Button(ventana,text="IMPAR",bg="green",fg="white",width=15,height=5,command=rang10)
b19.grid(column=3,row=3)
b20=Button(ventana,text="ROJOS",bg="red",fg="black",width=15,height=5,command=rang11)
b20.grid(column=3,row=4)
b21=Button(ventana,text="NEGROS",bg="black",fg="red",width=15,height=5,command=rang12)
b21.grid(column=3,row=5)
b22=Button(ventana,text="listo",bg="silver",fg="black",width=15,height=5,command=listo)
b22.grid(column=3,row=1)
b11.grid_forget()
b12.grid_forget()
b13.grid_forget()
b14.grid_forget()
b15.grid_forget()
b16.grid_forget()
b17.grid_forget()
b18.grid_forget()
b19.grid_forget()
b20.grid_forget()
b21.grid_forget()
b22.grid_forget()

ventana.mainloop()