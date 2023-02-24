def add(a,b):
    c=a+b 
    print("add is",c)
def multi(a,b):
    c=a*b
    print("multi is ",c)
def sub(a,b):
    c=a-b
    print("sub is ",c)
def div(a,b):
    c=a/b
    print("div is",c)
ch=int(input("enter a code"))
if ch==1:
    add(10,20)
elif ch==2:
    multi(20,30)
elif ch==3:
    sub(6,8)
elif ch==4:
    div(40,60)
else:
    print("code is invalid ")