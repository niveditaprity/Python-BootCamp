side1 = int(input("Enter the first side of triangle:"))
side2 = int(input("Enter the second side of triangle:"))
side3 = int(input("Enter the third side of triangle:"))
if side1 == side2 and side1 == side3:
    print("Equilateral triangle")
elif side1 != side2 and side1 != side3:
    print("Scalene triangle")
else:
    print("Isosceles triangle")
