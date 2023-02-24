def pr(n):
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

x=int(input("enter a num"))
pr(x)