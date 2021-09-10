from tkinter import*

def sub_ventana():
	sv=Toplevel()

vp=Tk()

b1=Button(vp,text="Abre ventana",command=sub_ventana)
b1.grid(row=0,column=0)

vp=mainloop()