amt=int(input("enter a amt"))
if amt<10000:
    dis=amt/100*10
elif amt<20000:
    dis=amt/100*15
else:
    dis=amt/100*20
total=amt-dis
print("your amount is ",amt)
print("your discount is ",dis)
print("your is total is ",total)

