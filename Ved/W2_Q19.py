a=int(input("Enter the age of first person:"))
b=int(input("Enter the age of second person:"))
c=int(input("Enter the age of third person:"))
d=int(input("Enter the age of fourth person:"))
if a>b and a>c and a>d:
    print("First person is oldest")
elif b>c and c>d:
    print("Second person is oldest")
elif c>d:
    print("Third person is oldest")
else :
    print("Fourth person is oldest")
