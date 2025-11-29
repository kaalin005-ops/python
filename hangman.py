import random

words = ("apple", "orange", "banana", "coconut", "pineapple", "guava")

# dictionary of keys
hangman_art = {
    0: ("    ",
        "    ",
        "    "),
    1: ("  0 ",
        "    ",
        "    "),
    2: ("  0 ",
        "  | ",
        "    "),
    3: ("  0 ",
        " /| ",
        "    "),
    4: ("  0 ",
        " /|\\",
        "    "),
    5: ("  0 ",
        " /|\\",
        " /  "),
    6: ("  0 ",
        " /|\\",
        " / \\"),
}

def display_man(wrong_guesses):
    print("****************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("******************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)

    wrong_guesses = 0
    guessed_letters = set()  # fixed typo and used a set to track unique guesses
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        # input validation: single alphabetic character
        guess = input("Enter a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue

        # avoid repeated guesses
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
        guessed_letters.add(guess)

        # reveal letters or count a wrong guess
        if guess in answer:
            for i, ch in enumerate(answer):
                if ch == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        # check win condition
        if "_" not in hint:
            display_man(wrong_guesses)
            print("You guessed it! The word was:", answer)
            is_running = False
            break

        # check lose condition (max 6 wrong guesses)
        if wrong_guesses >= 6:
            display_man(wrong_guesses)
            print("Out of guesses! The word was:", answer)
            is_running = False
            break

if __name__ == "__main__":
    main()
