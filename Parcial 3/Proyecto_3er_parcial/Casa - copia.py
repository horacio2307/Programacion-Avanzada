import serial
import time
from tkinter import*

arduino=serial.Serial('COM4',9600)
time.sleep(2)

def Patio():

    arduino.write('p'.encode())

def Casa():

    arduino.write('c'.encode())

def Zotano():

    arduino.write('z'.encode())

def Alarma():

    arduino.write('x'.encode())

def Fin():

    arduino.close()
    ventana.destroy()

ventana=Tk()
Texto=Label(ventana,text="3 leds = Intruso")
Texto.grid(row=2,column=3)
B_Patio=Button(ventana,text="Led Patio",command=Patio)
B_Patio.grid(row=1,column=1)
B_Casa=Button(ventana,text="Led Casa",command=Casa)
B_Casa.grid(row=1,column=2)
B_Zotano=Button(ventana,text="Led zotano",command=Zotano)
B_Zotano.grid(row=1,column=3)
B_Alarma=Button(ventana,text="Alarma",command=Alarma)
B_Alarma.grid(row=2,column=1)
Cerrar=Button(ventana,text="Cerrar",command=Fin)
Cerrar.grid(row=2,column=2)

ventana.mainloop()
