# 15. Write a program to find the lowest number out of two numbers excepted from user.
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
if a!=b:
    if a<b:
        print(f"{a} is lowest number")
    else:
        print(f"{b} is lowest number")
else:
    print("Both numbers are equal") 
