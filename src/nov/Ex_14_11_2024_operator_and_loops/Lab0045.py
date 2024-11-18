#Program to find max of three number

#Logic building

#user input -> num1,num2,num3 -> int
#o/p -> iNT OR STRING with max number

#Logic  If else -1 condition

#syntax  3 condition is there so using if,elif,elif
#if condition 1:
#  print("do 1")
#elif condition 2:
#  print("do 2")
#elif condition 3:
#  print("do 3")
#else :
#  print("do for else")

num1=int(input("Enter the first value\n"))  #5  ,# 10
num2=int(input("Enter the second value\n"))  #3 ,# 12
num3=int(input("Enter the third value\n"))   #2 ,#11

# 5>3 and  5>2
# num1>num2 and num1>num3 -> num1

# 12>10 and 12>11
# num2>num1 and num2>num3 -> num2

#when num1 num2 not greater then num3 will come

#num3

if num1>num2 and num1>num3:
   print("max is",num1)

elif num2>num1 and num2>num3:
    print("max is", num2)
else:
    print("max is", num3)

