n=int(input("enter a number "))
s=0
temp=n
while n!=0:
    r=n%10
    s=s+r*r*r
    n=int(n/10)
if temp==s:
    print(" armstrom")
else:
    print(" not arm")