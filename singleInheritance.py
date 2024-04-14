class A:
    def __init__(self,a,b):
        self.a=100
        self.b=200
        print("The __init__ method values are:",self.a,self.b)
    def add(self,c,d):
        return (self.a+self.b)*(c+d)
#obj=A()
#print(obj.add(10,20))

class B(A):
    def __init__(self,a,b,f):
        super().__init__(a,b)
        self.f=f
obj2=B(10,20,300)
print(obj2.f)


class C(A,B):
    def __init__(self,a,b,f,g):
        super().__init__(a,b,f)
        self.g=g
obj3=C(40,50,60,70)


