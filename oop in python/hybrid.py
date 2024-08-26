class p1:
    def input(self):
        self.a=int(input())
        self.b=int(input())
class p2(p1):
    def add(self):
        c=self.a+self.b
        print(c)
class p3(p1):
    def multi(self):
        z=self.a*self.b
        print(z)
p=p2()
p.input()
p.add()
n=p3()
n.input()
n.multi()
