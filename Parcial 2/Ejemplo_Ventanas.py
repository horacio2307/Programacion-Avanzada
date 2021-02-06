from tkinter import*

def imprimir():

    texto = Label(ventana,text="Hola mundo")
    texto.grid(column=0,row=0)


ventana = Tk()
boton=Button(ventana,text="Print",command=imprimir)
boton.grid(column=0,row=1)
ventana.mainloop()

