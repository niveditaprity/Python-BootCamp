# 14. Write a program to check whether a person is senior citizen or not.
age=int(input("Enter age: "))
if age<=0:
    print("Invalid age")
elif age>=60:
    print("Senior citizen")
else:
    print("Not a senior citizen")  
