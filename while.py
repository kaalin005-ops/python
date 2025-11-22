#execute some code while some condition remains true

name=input("Enter your name:")

if name==" ":
    print("you did not enter your name")
else: print(f"hello {name}")
#           |
#           |
#           |
#           |
#           👇

name=input("Enter your name:")
while name==" ":
    print("you did not enter your name:")
    name=input("Enter your name:")
print(f"hello {name}")

#           |
#           |
#           |
#           |
#           👇

num=int(input("Enter a #between 1-10:"))
while num <1 or num>10:
    print(f"{num} is not valid")
    num=int(input("Enter a # between 1-10:"))
print(f"your number is {num}")
