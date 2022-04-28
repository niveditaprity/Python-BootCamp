# 6. Write a program in Python to print the sum of first 5 even numbers
sum=0
for i in range(1,11):
    if i%2==0:
        sum+=i
print("Sum of 1st 5 even numbers= ",sum)
