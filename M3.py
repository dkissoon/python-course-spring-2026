import random

def letter_grade(score: int) -> str:
    """Return a letter grade for a numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    print("Assignment 3: Decisions and Loops Demo\n")

    # 1) Conditional structure (if/elif/else): letter grade
    while True:
        raw = input("Enter a test score (0-100): ").strip()
        if raw.lower() == "q":
            print("Quitting program.")
            return

        try:
            score = int(raw)
        except ValueError:
            print("Invalid input. Please enter a whole number, or 'q' to quit.")
            continue  # demonstrates control inside a loop

        if score < 0 or score > 100:
            print("Score must be between 0 and 100.")
            continue

        grade = letter_grade(score)
        print(f"Score: {score} -> Letter Grade: {grade}\n")
        break  # use of break after a valid score is entered

    # 2) For loop: process a sequence
    names = ["Alex", "Bri", "Casey", "Derek", "Evan"]
    print("For loop: Greeting a list of names")
    for i, name in enumerate(names, start=1):
        print(f"{i}. Hello, {name}!")
    print()

    # 3) While loop: guessing game until condition met
    secret = random.randint(1, 10)
    attempts = 0
    max_attempts = 5

    print("While loop: Guess the number (1-10)")
    print(f"You have {max_attempts} attempts. Type 'exit' to stop.\n")

    while attempts < max_attempts:
        guess_raw = input("Your guess: ").strip()

        if guess_raw.lower() == "exit":
            print("You chose to exit the guessing game.")
            break  # another break example

        try:
            guess = int(guess_raw)
        except ValueError:
            print("Please enter a number from 1 to 10.\n")
            continue  # continue example

        if guess < 1 or guess > 10:
            print("Out of range. Guess must be 1-10.\n")
            continue

        attempts += 1

        if guess == secret:
            print(f"Correct! The number was {secret}. You got it in {attempts} attempt(s).")
            break
        elif guess < secret:
            print("Too low.\n")
        else:
            print("Too high.\n")
    else:
        # This runs only if the while loop ends normally (no break)
        print(f"Out of attempts! The number was {secret}.")

    print("\nProgram finished.")

if __name__ == "__main__":
    main()
