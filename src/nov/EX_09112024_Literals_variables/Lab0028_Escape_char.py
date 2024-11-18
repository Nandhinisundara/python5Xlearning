#Difference between '' and ""

# dir='c:\pramod\n.txt' # here \n is new line
# dir="c:\pramod\t.txt" # \t is tab space

#error will come to avoid this we are using 'r' raw string

dir=r'c:\pramod\n.txt'
dir=r"c:\pramod\t.txt"

print(dir) # it will print as it is because of r
