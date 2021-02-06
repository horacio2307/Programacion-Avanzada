from tkinter import*

ventana = Tk()

ventana.geometry("650x404")

i=PhotoImage(file="LC103-1.gif")

l=Label(ventana,image=i)
l.grid(column=30,row=50)

Button(ventana,text="Hola").grid(column=0,row=0)



ventana.mainloop()

