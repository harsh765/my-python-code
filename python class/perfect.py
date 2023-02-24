n=int(input("enter a number"))
c=0
a=1
while a<n:
    r=n%a
    if r==0:
        c=c+a
    a=a+1
    print(c)
if c==n:
    print("perfect")
else:
    print("not perfect")