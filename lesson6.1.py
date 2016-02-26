
from abc import ABCMeta, abstractmethod, abstractproperty

class A(object):
    __metaclass__=ABCMeta
    x = 0   

class Number(object):
    x = int(raw_input('Enter number from 1 to 9\n'))
    
    def __init__(self):
        self.x = self.x

    def mult(self):
        n1 = str(input("Enter several numbers\n"))
        n2 = int(input("How many times repeat?\n"))
        return(n1*n2)

    def power(self):
        n1 = input("Raising to the power\n")
        return(self.x ** n1)

    def loop(self,x,z):
        z = [x for x in range(x, x + 10)]
        return(x)

class Ch(Number):
    def __init__(self):
        self.x = self.x
        pass
        super(Ch,self).__init__()

f = Ch()
if f.x in range(1, 4):
    print(f.mult())
elif f.x in range(3, 8):
    print(f.power())
elif f.x in range(7, 10):
    print(f.loop())
else:
    print("Error")


raw_input()