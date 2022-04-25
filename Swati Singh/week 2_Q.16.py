# 16. Write a program to check whether a number (accepted from user) is positive or negative.
num=int(input("Enter a number: "))
if num==0:
    print("Neither positive nor negative number")
elif num>0:
    print("Positive number")    
else:
    print("Negative number")  
