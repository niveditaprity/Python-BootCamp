unit = int(input("Enter units consumed: "))
price = 0
if unit>200:
    price = (unit-200)*10 + (unit-(unit-200)-100)*5
if unit>100 and unit<=200:
    price = (unit-100)*5
if unit <100:
    pass
print('charge = ',price)
