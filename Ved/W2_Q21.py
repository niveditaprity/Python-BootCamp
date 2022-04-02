sal=int(input("Enter your salary:"))
yer=int(input("Enter time period of your service(in years):"))
if yer>10:
    bns1=sal*10/100
    net1=sal+bns1
    print("You will receive",net1)
elif yer>=6:
    bns2=sal*8/100
    net2=sal+bns2
    print("You will receive",net2)
else:
    bns3=sal*5/100
    net3=sal=bns3
    print("You will receive",net3)
