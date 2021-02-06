import time

class suma:

    def __init__ (self):

        pass


    def suma(self,a,b):
        global r
        r=a+b
        print (r)

class resta:

    def __init__(self,a,b):

        self.a=a
        self.b=b

    def resta(self):

        r=self.a-self.b

        print(r)

class mult:

    def __init__(self,a,b):

        self.a=a
        self.b=b

    def mult(self):

        r=self.a*self.b

        print (r)

O1=suma()
O2=resta(10,5)
O3=mult(10,5)
r=0
O1.suma(10,5)
time.sleep(1);
print(r)
time.sleep(1)
O2.resta()
time.sleep(1)
print(r)
time.sleep(1)
O3.mult()
time.sleep(1)
print (r)
