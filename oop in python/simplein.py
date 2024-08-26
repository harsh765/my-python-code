# class prog:
#     def input(self):
#         self.a=int(input("enter a num"))
#         self.b=int(input("enter a num"))
# class prog2(prog):
#     def add(self):
#         c=self.a+self.b
#         print(c)
# p=prog2()
# p.input()
# p.add()


# class prog:
#     def input(self):
#         self.a=int(input("enter a num"))
#         self.b=int(input("enter a num"))
# class prog2(prog):
#     def add(self):
#         c=self.a+self.b
#         print(c)
# class prog3(prog):
#     def muti(self):
#         c=self.a*self.b
#         print(c)
# p2=prog2()
# p2.input()
# p2.add()
# p3=prog3()
# p3.input()
# p3.muti()


# class prog:
#     def input(self):
#         self.a=int(input())
#         self.b=int(input())
# class prog2:
#     def input2(self):
#         self.x=int(input())
#         self.y=int(input())
# class prog3(prog,prog2):
#     def add(self):
#         c=self.a+self.b
#         print(c)
#         z=self.x*self.y
#         print(z)
# p=prog3()
# p.input()
# p.input2()
# p.add()

class mark:
    def inputinfo(self):
        self.roll=int(input("enter a roll no"))
        self.name=input("enter a name")
class m2(mark):
    def ma(self):
        self.m1=int(input("enter a m1 "))
        self.m2=int(input("enter a m1 "))
        self.m3=int(input("enter a m3 "))
class m3(m2):
    def to(self):
        print(self.roll,self.name)
        self.total=self.m1+self.m2+self.m3
        print("total is ",self.total)
        per=self.total/3
        print("percentage is ",per)
pe=m3()
pe.inputinfo()
pe.ma()
pe.to()
