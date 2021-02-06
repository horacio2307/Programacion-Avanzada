class calcu():
    def __init__(self):
        pass

    def menu(self):

        a=0

        while (a!=9):

            try:

                a=int(input("\nSelecciona \n0 --> Suma\n1 --> Resta\n\n"))

            except ValueError:

                a=3

            if(a>-1 and a<2):

                b = int(input("\nIngresa el primer numero\n\n"))

                c = int(input("\nIngrese el segundo numero\n\n"))

                z=self.diccionario(a,b,c)

                print(z)

            else:
                pass

    def diccionario(self,x,b,c):

        w={
            0: b+c,
            1: b-c,
        }

        return w.get(x,"Nada")

cal=calcu()
cal.menu()
            