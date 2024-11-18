#Problem to find the max between two ( 3,4) → 4

#Logic building formala
#1. user input  -> two integer
#2. output-> 1 INT which is greater it will display
#3 safe side for float value also using float data type
num1=float(input("Enter the first value:"))
num2=float(input("Enter the second value:"))

if num1>=num2:

    print("max is",num1)

else:
    print("max is",num2)

#4 Edge case -> num1=num2 -> this is handled
# string -> ABC -> try and except
# Negative value

