class prog:
    def add(self,a,b):
        c=a+b
        print(c)
    def add(self,a,b,c):
        z=a+b+c
        print(z)
x=int(input("enter a number"))
y=int(input("enter a number"))
h=int(input("enter a number"))
p=prog()
p.add(x,y)
p.add(x,y,h)