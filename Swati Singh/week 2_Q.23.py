# 23. Write a program to accept percentage and display the Category according to the following criteria :
     ##  Percentage          Category 
     ##  < 40                Failed
     ##  >=40 & <55            Fair 
     ##  >=55 & <65            Good 
     ##  >=65                 Excellent
percentage=int(input("Enter the percentage: "))
if percentage>=65:
    print("Excellent")
elif 55<=percentage<65:
    print("Good") 
elif 40<=percentage<55:
    print("Fair")
else:
    print("Fail")
