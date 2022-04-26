# 24. Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.
     ##  Note :
     ##  An equilateral triangle is a triangle in which all three sides are equal.
     ##  A scalene triangle is a triangle that has three unequal sides.
s1=int(input("Enter 1st side of the triangle: "))
s2=int(input("Enter 2nd side of the triangle: "))
s3=int(input("Enter 3rd side of the triangle: "))
if s1==s2==s3:
    print("It is an euilateral triangle.")
elif s1==s2 or s2==s3 or s3==s1:
    print("It is an isosceles triangle.") 
else:
    print("It is a scalene triangle.") 
