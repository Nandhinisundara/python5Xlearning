#write a program to take a user age and let him know  if he can go to  club 21 age

#step 1
#user input i/p -> data type INT
# o/p -> string -> he can go to club or not

# step2 rough logic
# age>21  he can go
# age<21  he cannot go

#step 3 write the logic

person =int(input("enter the age of the person:"))

if person>=21:
    print("He can go to the club")

else:
    print("He is not allowed to go club")

# step 4 check the edge case
# we should consider the edge case such as
#Negative ages or extremely high values -> program will break
# non alpha numeric like abc
# age which is valid
# print("He can go to club" if person>=21 else "He is not allowed to go club")

