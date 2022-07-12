# using rand int, instead of a list. Way more cleaner 
import random

attempts = 0

def pick_random_number() -> int:
    """We can return a random number from the list"""
    random_number = random.randint(1,100)
    return random_number

random_number = pick_random_number()

def game_logic(num, guess, attempts):
    """This is just telling the user whether their guess was too high or too low, or if they got the right answer"""
    if guess < num:
        print("Too low.")
        print("Guess again.")
        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
    elif guess > num:
        print("Too high.")
        print("Guess again.")
        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
    else:
        print(f"You got it! The answer was {num}!")
        return False


# start of our game
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
if choice.lower() == 'hard':
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
elif choice.lower() == 'easy':
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
else:
    attempts = 10
    print(f"I don't understand what {choice} means, but I'm just going to give you easy mode.")


game_on = True

while game_on:
    # only subtracting from our attempts count when user enters an integer
    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("\n\nThe guess must be a whole number!!!")
        continue

    print("\n\n") # strictly for the command line so it doesn't all look so clumped together

    attempts -= 1
    outcome = game_logic(random_number, guess, attempts)
    
    if attempts == 0:
        print("You've run out of guesses. You lose.")
        game_on = False

    if outcome == False:
        game_on = False

