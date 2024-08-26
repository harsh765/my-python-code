a=int(input("enter a num"))
b=int(input("enter a number "))
try:
    c=a/b
    print(c)
except ValueError:
    print("do not divide by zero")
print("programm end")


# a=10
# b="1111"
# try:
#     c=b/a
#     print(c)
# except Exception:
#     print("valid num")
# print("end progg")

# a=int(input())
# b=int(input())
# c=a/b
# print("div is",c)