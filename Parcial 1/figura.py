global v

class circulo:

    def __init__(self,radio,base,altura):  #Creador

        self.radio=radio #atributo   describe el objeto
        self.base=base
        self.altura=altura

    def area(self):      #Creamos metodo

        area=3.1415*pow(self.radio,2)

        print("EL área del círculo es :\t" , area)


class rectangulo:

    def __init__(self,radio,base,altura,):

        self.radio=radio

        self.base=base

        self.altura=altura

    def area(self):
        
        a=self.base*self.altura

        print("Area:\t" , a, "\n")

    def perimetro(self):

        p=(2*self.base)+(2*self.altura)

        print("perimetro:\t" ,p, "\n")


class figura(rectangulo,circulo):

             def valores_multi(self):
                 global v
                 v=self.radio*self.base*self.altura

                 return v
                 
                 
