import random

print("⚂ Dice Roller 🎲")
is_running = True

while is_running:
    user_input = input("Press Enter to roll the dice or type 'q or quit' to exit: ").lower()

    if user_input == "q":
        print("Thanks for playing! Goodbye 👋")
        is_running = False
    else:
        # Roll a single six-sided dice
        result = random.randint(1, 6)
        print(f"You rolled: {result}")