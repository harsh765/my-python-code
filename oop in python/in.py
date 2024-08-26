# class person:
#     a=10
#     b=20
#     print(a,b)
# class deri(person):
#     print("hello")
    
# p=person()

class base:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def add(self):
        c=self.a+self.b
        print(c)
class deri(base):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.m=x
        self.n=y
    def multi(self):
        l=self.m*self.n
        print(l)
p=deri(10,5)
p.add()
p.multi()