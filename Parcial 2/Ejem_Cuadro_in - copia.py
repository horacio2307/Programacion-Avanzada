from tkinter import*

def obtener():

    texto = t.get()
    l=Label(ventana,text=texto) #Borrar state=DISABLE  // Ya lo borre
    #l.grid(column=0,row=2)
    l.place(x=0,y=80)
    cuadro.config(state=NORMAL) #Activar el cuadro

ventana = Tk()
ventana.config(width=900,height=500)
b = Button(ventana,text="Enter",command=obtener,width=10,height=10) #Borrar state=DISABLE // Ya lo borre
#b.grid(column=0,row=1)
b.place(x=100,y=50)
t = StringVar()
cuadro = Entry(ventana,textvariable=t,show=("*"),state=DISABLED,bd=15,width=100) #Entra valor 
#cuadro.grid(column=0,row=0)
cuadro.place(x=0,y=0)


ventana.mainloop()


