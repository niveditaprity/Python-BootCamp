# 18. Accept the age of 4 people and display the youngest one?
a1=int(input("Enter the age of 1st person: "))
a2=int(input("Enter the age of 2nd person: "))
a3=int(input("Enter the age of 3rd person: "))
a4=int(input("Enter the age of 4th person: "))
if a1<a2 and a1<a3 and a1<a4:
    print(f"1st person is the youngest with age {a1}")
elif a2<a1 and a2<a3 and a2<a4:
    print(f"2nd person is the youngest with age {a2}")    
elif a3<a1 and a3<a2 and a3<a4:
    print(f"3rd person is the youngest with age {a3}")
else:
    print(f"4th person is the youngest with age {a4}")
