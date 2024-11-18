#Grade calculator
#write a program that calculate and display the letter grade  numerical score
#(A,B,C,D,E,F)  based on folling score

#Logic building formula

#step 1
# user input -> score or marks ->int
# o/p -> string -> A or B

score =int(input("Enter your score"))

#step 2 rough logic

# score >=90 and score <=100 -> A
# score >=80 and score <=89 -> B
# score >=70 and score <=79 -> c
# score >=60 and score <=69 -> d
# score >=0 and score <=59 -> A

if score >=90 and score <=100:
    print("your grade is A")
elif score >=80 and score <=89:
    print("your grade is A")
elif score >=70 and score <=79:
    print("your grade is A")
elif score >=60 and score <=69:
    print("your grade is A")
elif score>=100 and score <=-1:
    print("your grade is superman you can't get a grade")
else:
    print("your grade is Fail")

#special charcter

#more than 100
#less than 100
#negative num