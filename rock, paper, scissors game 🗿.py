import random

# Choices available
choices = ["rock", "paper", "scissors"]

print("🗿 Rock, Paper, Scissors Game ✂️📄")
print("Type 'quit' anytime to exit.\n")

player_score = 0
computer_score = 0

while True:
    # Player input
    player = input("Enter rock, paper, or scissors: ").lower()

    if player == "quit":
        print("Game Over!")
        print(f"Final Score → You: {player_score}, Computer: {computer_score}")
        break

    if player not in choices:
        print("Invalid choice. Please try again.\n")
        continue

    # Computer choice
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    # Decide winner
    if player == computer:
        print("It's a tie!\n")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("🎉 You win!\n")
        player_score += 1
    else:
        print("💻 Computer wins!\n")
        computer_score += 1