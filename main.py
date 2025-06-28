import random
import art
NUM1 = 1
NUM2 = 100

def guessing(amount):
    number_to_guess = random.randint(NUM1, NUM2)
    while amount > 0:
        print(f"You have {amount} guesses remaining.")
        user_guess = int(input("What's your guess?: "))
        if user_guess == number_to_guess:
            print(f"Congrats, you guessed the correct number {number_to_guess}. You win!")
            break
        elif user_guess > number_to_guess:
            print("You guessed too high.")
        elif user_guess < number_to_guess:
            print("You guessed too low.")
        amount -= 1
    print(f"You ran out of guesses. You lose!")

print(art.another_logo)
print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {NUM1} and {NUM2}.")
difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()


if difficulty == "easy":
    guess_amount = 10
    guessing(guess_amount)
elif difficulty == "hard":
    guess_amount = 5
    guessing(guess_amount)
else:
    print("Invalid difficulty.")
