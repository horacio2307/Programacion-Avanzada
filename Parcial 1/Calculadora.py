class suma:
    def __init__(self):
        pass
    
    def suma(self,a,b):
        print("La suma es: \t ",a+b,"\n")

class resta:
    def __init__ (self):
        pass

    def resta(self,a,b):
        print("La resta es: \t",a-b,"\n")

class multi:
    def __init__ (self):
        pass

    def multi(self,a,b):
        print("La multiplicacion es: \t",a*b,"\n")

class div:
    def __init__ (self):
        pass

    def div(self,a,b):
        try:
            r=a/b
            print("La division es: \t",r,"\n")

        except ZeroDivisionError:
            print("Ingrese otros datos")

class calculadora(suma,resta,multi,div):
    def encendido(self):
        o="e"
        
        while(o!="u"):
            o=input("Selecciona:\n\ts --> suma\n\tr --> resta\n\tm --> multiplicacion\n\td --> division\n\tu --> salir\n")
            if(o=="u"):
                print("The end")
                
            else:
                if(o=="u"):
                    pass
                else:
                    a=int(input("\nIngresa el primer numero\n"))
                    b=int(input("\nIngrese el segundo numero\n"))
                    if(o=="s"):
                        self.suma(a,b)
                    if(o=="r"):
                        self.resta(a,b)
                    if(o=="m"):
                        self.multi(a,b)
                    if(o=="d"):
                        self.div(a,b)

calculadora1=calculadora()
calculadora1.encendido()