# 3. Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not
num=int(input("Enter a number: "))
rem=num%10
if rem%3==0:
    print("Last digit is divisible by 3")
else:
    print("Last digit is not divisible by 3") 
