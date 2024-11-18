#Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine if the
# triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or
# scalene (no sides are equal). Use an if-else statement to classify the triangle.

#step 1
#i/p -> side1,side2,side3 -> INT
#o/p-> string -> equal or iso or scalene

side1=int(input("Enter the side1"))
side2=int(input("Enter the side2"))
side3=int(input("Enter the side3"))

#step2 rough logic

#side1=side2=side3 -> equalateral triangle
#side1=side


if side1== side2 ==side3:
    print("equilateral")
elif(side1 == side2 != side3) or (side1!= side2 == side3) or (side1==side3 != side2):
    print("isosceles")
else:
    print("scalene")