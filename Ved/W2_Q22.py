mrk_prc=int(input("Enter the marked price:"))
if mrk_prc>10000:
    dic1=mrk_prc*20/100
    net1=mrk_prc-dic1
    print("You have to pay:",net1)
elif mrk_prc>7000:
    dic2=mrk_prc*15/100
    net2=mrk_prc-dic2
    print("You have to pay:",net2)
else:
    dic3=mrk_prc*10/100
    net3=mrk_prc-dic3
    print("You have to pay:",net3)
