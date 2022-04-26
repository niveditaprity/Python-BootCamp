# 22. Accept the marked price from the user and calculate the Net amount as(Marked Price – Discount) to pay according to following criteria:
     ##  Marked Price           Discount
     ##  10000                  20%
     ##  7000 and <=10000       15% 
     ##  <=7000                 10%
MP=int(input("Enter marked price: "))
if MP>10000:
    dis=MP*0.20
elif 7000<MP<=10000:
    dis=MP*0.15
else:
    dis=MP*0.10
Net_amt=MP-dis
print("Net amount= ",Net_amt) 
