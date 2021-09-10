from tkinter import*

global sv

def sub_ventana():
    global sv
    sv=Toplevel()
    b2=Button(sv,text="Cerrar",command=cerrar)
    b2.grid(row=0,column=0)

def cerrar():
    global sv
    b3=Button(vp,text="Reabrir",command=abrir)
    b3.grid(row=0,column=1)
    sv.withdraw()

def abrir():
    
    global sv
    sv.deiconify()


vp=Tk()
b1=Button(vp,text="Abre ventana",command=sub_ventana)
b1.grid(row=0,column=0)

vp.mainloop()