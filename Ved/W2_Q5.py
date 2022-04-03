unit=int(input("Enter the unit:"))
if unit<=100:
    print("No charges")
elif unit<=200:
    U=unit-100
    P=5*U
    print("Rs",P)
else :
    S=100*5
    T=unit-200
    C=T*10
    A=S+C
    print("Rs",A)
