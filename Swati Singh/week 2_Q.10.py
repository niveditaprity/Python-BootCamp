# 10. Write a program to check whether an year is leap year or not. 
year=int(input("Enter an year : "))
if (year%4==0) and (year%100!=0) or (year%400==0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")   
