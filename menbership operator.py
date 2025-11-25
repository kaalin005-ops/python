#membership operator=used to test  whether a value or variable is found in a sequence
#                    (string,list,tuble,set or dictionary)

#                    1.in
#                    2.not in

'''word="Apple"
letter=input("Guess a letter in the secret word")

if letter not in word:
    print(f"there is a {letter}")
else:
    print(f"{letter} was not found")
'''

students={"spongebob","ppguig","sandy"}
student=input("enter the name of a student")

if student in  students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")

#grades

grades={"sandy":"A",
        "squid":"B",
        "sponge":"C","patrick":"D"}

student=input("Enter the name of a student:")
if student in grades:
    print(f"{student}'s grade is {grade[student]}")
else:
    print(f"{student} was not found")