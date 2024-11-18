# if your age is greater tham 18 allowed to vote

person1=int(input("enter your age"))

# normal if else statement  use this

# if person1>=18:
#      print("you are eligible to  vote")
# else:
#      print("not eligible to vote")

print("you are eligible to vote" if person1>=18 else "not eligible to vote")  # avoid one line code

# ternary operator in single line it will come