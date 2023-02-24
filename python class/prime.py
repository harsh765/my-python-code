n=int(input("enter a number"))
c=0
a=1
while a<=n:
    r=n%a
    if r==0:
        c=c+1
    a=a+1
if c==2:
    print("prime")
else:
    print("not prime")