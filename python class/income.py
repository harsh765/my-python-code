amt=int(input("enter a amt"))
if amt<300000:
    tax=0
elif amt<600000:
    tax=amt/100*5
elif amt<900000:
    tax=amt/100*10
elif amt<1200000:
    tax=amt/100*15
else:
    tax=amt/100*20
total=amt-tax
print("your amount is ",amt)
print("your tax is ",tax)
print("your is total is ",total)

