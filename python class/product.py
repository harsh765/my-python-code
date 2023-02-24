co=int(input("enter a code"))
amt=int(input("enter a amt"))
if co==1:
    if amt<1000:
        dis=amt/100*20
        
    else:
        dis=0
elif co==2:
    if amt<500:
        dis=amt/100*10
    else:
        dis=0
elif co==3:
    if amt<100:
        dis=amt/100*5
    else:
        dis=0
else:
    dis=0
to=amt-dis
print("amt is ",amt)
print("discount is ",dis)
print("total is ",to)