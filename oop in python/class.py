# class prog:
#     a=10
#     b=20
# p=prog()
# print(p.a)
# print(p.b)

# class person:
#     def __init__(self,fname,lname):
#         self.fristname=fname
#         self.lastname=lname
#     def printname(self):
#         print(self.fristname,self.lastname)
# x=person("john","doe")
# x.printname()


# class person:
#     f=""
#     l=""
#     def __init__(fname,lname):
#         f=fristname=fname
#         l=lastname=lname
#     def printname():
#         print(f,l)

# x=person("sunny","raj")
# x.printname()


class person:
    def __init__(self,a,b):
      self.s=a-b
      self.g=a+b
      self.c=a*b
      self.h=a/b
    def add(self):
      print(self.g)
    def multi(self):
       print(self.c)
    def sub(self):
       print(self.s)
    def div(self):
       print(self.h)
p=person(10,20)
p.add()
p.multi()
p.sub()
p.div()


    