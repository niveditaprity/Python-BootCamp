i = int(input("Enter the cost price of bike: "))
if i>100000:
    print('Tax = ',0.15*i)
elif i>50000 and i<=100000:
    print('Tax =',0.10*i)
else:
    print('Tax = ',0.05*i)
