# try:
#     fileptr=open("fil.txt","r")
#     if fileptr:
#         print("file is opened successfully ")
#     else:
#         print ("file not found")
#         fileptr.close()
# except FileNotFoundError:
#     print("file not found")
# print("programm end")

# try:
#     a=["sunny","harsh","prasad"]
#     i=0
#     while i<7:
#         print(a[i])
#         i=i+1
# except IndexError:
#     print("value are to much")
# print("end prog")


try:
    a=int(input())
    b=int(input())
    c=a/b
    print(c)
finally:
    print("do not divide zero")
