class p1:
    def input(self):
        self.a=int(input("enter a number"))
        self.b=int(input("enter a number"))
class p2(p1):
    def add(self):
        c=self.a+self.b
        print(c)
class p3(p2):
    def muti(self):
        d=self.a*self.b
        print(d)
class p4(p3):
    def sub(self):
        e=self.a-self.b
        print(e)
p=p4()
p.input()
p.add()
p.muti()
p.sub()
