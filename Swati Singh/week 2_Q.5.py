# 5. Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : Unit Price
    ## First 100 units no charge Next 100 units Rs 5 per unit After 200 units Rs 10 per unit (For example if input unit is 350 than total bill amount is Rs2000)
units=int(input("Enter the number of unit of electricity used: "))  
if units<=100:
    bill=0
elif 100<units<=200:
    bill=(units-100)*5
elif units>200:
    bill=100*5+(units-200)*10
print("Total electricity bill = ",bill)
