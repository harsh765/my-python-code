class prog1:
    def input(self):
        self.a=int(input("="))
        self.b=int(input("="))
class prog2(prog1):
    def add(self):
        self.c=self.a+self.b
class prog3(prog1):
    def multy(self):
        self.z=self.a*self.b
class prog4(prog2,prog3):
    def printall(self):
        print(self.c)
        print(self.z)
p=prog4()
p.input()
p.add()
p.multy()
p.printall() 