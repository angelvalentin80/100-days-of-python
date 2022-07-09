# my solution
import random

game_list = ["rock", "paper" , "scissors"]
computer_rng = random.randint(0,2)


player_number= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

player_choice = game_list[player_number]
computer_choice = game_list[computer_rng]


print(f"You chose:\n\n\n {player_choice}\n")
print(f"The computer chose:\n\n\n {computer_choice}\n")


if player_number == 0 and computer_rng == 1:
    print("You lose")
elif player_number == 0 and computer_rng == 2:
    print("You win")
elif player_number == 1 and computer_rng == 0:
    print("You win")
elif player_number == 1 and computer_rng == 2:
    print("You lose")
elif player_number == 2 and computer_rng == 0:
    print("You lose")
elif player_number == 2 and computer_rng == 1:
    print("You win")
elif player_number == computer_rng:
    print("You and the computer tied")
else:
    print("I don't understand that command")
