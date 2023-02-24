def fact(n):
    s=1
    a=1
    while a<=n:
        s=s*a
        a=a+1
    return(s)
n=int(input("enter a num"))
z=fact(n)
print(z)
