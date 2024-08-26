class base:
    def inputdata(self):
        self.a=int(input("Enter any value"))
        self.b=int(input("Enter any value"))
class deri1(base):
    def add(self):
        c=self.a+self.b
        print(c)
class deri2(deri1):
    def multi(self):
        c=self.a*self.b
        print(c)
d=deri2()
d.inputdata()
d.add()
d.multi()