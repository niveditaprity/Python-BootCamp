cst_prc=int(input("Enter the cost price of the bike:"))
if cst_prc>100000:
    tax1=cst_prc*15/100
    print("The road tax is ",tax1)
elif cst_prc>50000:
    tax2=cst_prc*10/100
    print("The road tax is ",tax2)
elif cst_prc<=50000 and cst_prc>0:
    tax3=cst_prc*5/100
    print("The road tax is ",tax3)
else:
    print("Enter correct cost price")
