
# def fact(n):
#     s=1
#     a=1
#     while a<=n:
#         s=s*a
#         a=a+1
#     print(s)
# n=int(input("enter a num"))
# fact(n)
 
def rev(n):
    s=0
    t=n
    while n>0:
        r=n%10
        s=s*10+r
        n=int(n/10)
    print(s)
i=int(input("enter a num"))
rev(i)


