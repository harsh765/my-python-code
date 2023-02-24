def add(a,b):
    c=a+b
    return(c)
def multi(a,b):
    c=a*b
    return(c)
def sub(a,b):
    c=a-b
    return(c)
def div(a,b):
    c=a/b
    return(c)
x=int(input("enter a num"))
y=int(input("enter a num"))
z=add(x,y)
print("add is ",z)
z=multi(x,y)
print("muti is ",z)
z=sub(x,y)
print("sub is ",z)
z=div(x,y)
print("div is ",z)