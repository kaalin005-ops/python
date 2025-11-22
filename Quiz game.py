questions = [
    "How many elements are in the periodic table?",
    "Which animal lays eggs?",
    "How many bones are in the human body?"
]

options = [
    ("A.116", "B.117", "C.118", "D.119"),
    ("A.Whale", "B.Crocodile", "C.Elephant", "D.Ostrich"),
    ("A.206", "B.207", "C.208", "D.209")
]

answers = ["C", "D", "A"]

guesses = []
score = 0
question_num = 0

for question_num, question in enumerate(questions):
    print("____________________")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("You guessed correctly!")
    else:
        print("Incorrect.")
        print(f"The correct answer was {answers[question_num]}.")
    print()

print("_________________")
print("     RESULT      ")
print("_________________")

print("Answers: ", end=" ")
for ans in answers:
    print(ans, end=" ")
print()

print("Guesses: ", end=" ")
for g in guesses:
    print(g, end=" ")
print()

score_percent = int(score / len(questions) * 100)
print(f"Your score is: {score_percent}%")