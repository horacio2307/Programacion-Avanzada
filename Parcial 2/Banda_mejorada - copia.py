from tkinter import*

global chicas
global medianas
global grandes
global total

chicas = medianas = grandes = total = 0
alto = 2
alto2 = 1

def iniciar_banda():

    global chicas
    global medianas
    global grandes
    global total    
    chicas = medianas = grandes = total = 0
    Cajas_Chicas.config(state=NORMAL)
    Cajas_Medianas.config(state=NORMAL)
    Cajas_Grandes.config(state=NORMAL)
    Print_c.config(state=NORMAL)
    Print_m.config(state=NORMAL)
    Print_g.config(state=NORMAL)
    Print_t.config(state=NORMAL)
    Fin.config(state=NORMAL)
    Inicio.config(state=DISABLED)
    Sc = Label(ventana,text=chicas,width=10,height=alto2)
    Sc.place(x=90,y=65)
    Sm = Label(ventana,text=medianas,width=10,height=alto2)
    Sm.place(x=90,y=90)
    Sg = Label(ventana,text=grandes,height=alto2,width=10)
    Sg.place(x=90,y=115)
    St = Label(ventana,text=total,width=10,height=alto2)
    St.place(x=90,y=140)

def end_banda():
    
    Cajas_Chicas.config(state=DISABLED)
    Cajas_Medianas.config(state=DISABLED)
    Cajas_Grandes.config(state=DISABLED)
    Print_c.config(state=DISABLED)
    Print_m.config(state=DISABLED)
    Print_g.config(state=DISABLED)
    Print_t.config(state=DISABLED)
    Inicio.config(state=NORMAL)
    Fin.config(state=DISABLED)

def c_chicas():

    global chicas 
    global total

    chicas = chicas + 1
    total = total + 1

    Sc = Label(ventana,text=chicas,width=10,height=alto2)
    Sc.place(x=90,y=65)

    St = Label(ventana,text=total,width=10,height=alto2)
    St.place(x=90,y=140)

def c_medianas():

    global medianas
    global total

    medianas = medianas + 1
    total = total + 1

    Sm = Label(ventana,text=medianas,width=10,height=alto2)
    Sm.place(x=90,y=90)

    St = Label(ventana,text=total,width=10,height=alto2)
    St.place(x=90,y=140)

def c_grandes():

    global grandes
    global total

    grandes = grandes + 1
    total = total + 1

    Sg = Label(ventana,text=grandes,height=alto2,width=10)
    Sg.place(x=90,y=115)

    St = Label(ventana,text=total,height=alto2,width=10)
    St.place(x=90,y=140)

ventana = Tk()
ventana.title("Banda de cajas")
ventana.geometry("200x200")
Inicio = Button(ventana,text="Run",width=10,height=alto,command=iniciar_banda)
Fin = Button(ventana,text="Stop",width=10,height=alto,state=DISABLED,command=end_banda)
Cajas_Chicas = Button(ventana,text="Chica",command=c_chicas,width=6,height=alto2,state=DISABLED)
Cajas_Medianas = Button(ventana,text="Mediana",command=c_medianas,width=8,height=alto2,state=DISABLED)
Cajas_Grandes = Button(ventana,text="Grande",command=c_grandes,width=6,height=alto2,state=DISABLED)
Print_c = Label(ventana,text="Cajas chicas:",width=12,height=alto2,state=DISABLED)
Print_m = Label(ventana,text="Cajas medianas:",width=12,height=alto2,state=DISABLED)
Print_g = Label(ventana,text="Cajas grandes :",width=12,height=alto2,state=DISABLED)
Print_t = Label(ventana,text="Cajas totales:",width=12,height=alto2,state=DISABLED)

Inicio.place(x=0,y=0)
Fin.place(x=76,y=0)
Cajas_Chicas.place(x=0,y=40)
Cajas_Medianas.place(x=45,y=40)
Cajas_Grandes.place(x=104,y=40)
Print_c.place(x=0,y=65)
Print_m.place(x=0,y=90)
Print_g.place(x=0,y=115)
Print_t.place(x=0,y=140)

ventana.mainloop()



