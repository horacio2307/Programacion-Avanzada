from tkinter import*

def suma():

    a=int(input("\nIngrese primer numero\n"))

    b=int(input("\nIngrese segundo numero\n"))

    lsuma=Label(ventana,text=a+b)
    lsuma.grid(column=4,row=0)

def resta():

    a=int(input("\nIngrese primer numero\n"))

    b=int(input("\nIngrese segundo numero\n"))

    lresta=Label(ventana,text=a-b)
    lresta.grid(column=4,row=0)

def mult():

    a=int(input("\nIngrese primer numero\n"))

    b=int(input("\nIngrese segundo numero\n"))

    lmult=Label(ventana,text=a*b)
    lmult.grid(column=4,row=0)

def division():

    a=int(input("\nIngrese primer numero\n"))

    b=int(input("\nIngrese segundo numero\n"))

    try:

        lsuma=Label(ventana,text=a/b)
        lsuma.grid(column=4,row=0)

    except ZeroDivisionError:

        lsuma=Label(ventana,text="Error de division, no se puede dividir entre 0")
        lsuma.grid(column=4,row=0)

ventana=Tk()
ventana.title("Calculadora Basica")
ventana.geometry("450x500")

b_suma=Button(ventana,text="Suma",command=suma)
b_suma.grid(column=0,row=3)

b_resta=Button(ventana,text="Resta",command=resta)
b_resta.grid(column=1,row=3)

b_multi=Button(ventana,text="Multiplicacion",command=mult)
b_multi.grid(column=2,row=3)

b_div=Button(ventana,text="Division",command=division)
b_div.grid(column=3,row=3)

ventana.mainloop()