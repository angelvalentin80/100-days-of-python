
## my solution

print("Welcome to Treasure Island!\nYour mission is to find the treasure.")

left_or_right = input('You' + "'" + 're at a cross road. Where do you want to go? Type "left" or "right"\n')

if left_or_right.lower() == "left":
    wait_or_swim = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if wait_or_swim.lower() == "wait":
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if color.lower() == "red":
            print("It's a room full of fire.Game Over.")
        elif color.lower() == "yellow":
            print("You found a yellow floaty that you can use to swim home. Game Over. No more options. Sorry")
        elif color.lower() == "blue":
            print("You found Matt Damon, he's going to take you home in his private jet and give you 1 million dollars. Game Over.")
        else:
            print("I don't know that command")

    elif wait_or_swim.lower() == "swim":
        print("You just swam and shark came by and ate you. Yes a lot of endings end short because these if statements are torture")
    else:
        print("I don't know that command")



elif left_or_right.lower() == "right":
    jump_or_walk = input('You just walked toward the edge of a huge water fall. Type "jump" to jump 100 feet into some water. Type "walk" to walk to a different location\n')
    if jump_or_walk.lower() == "jump":
        print("You just jumped to your death. The water was shallow!")
    elif jump_or_walk.lower() == "walk":
        print("You found a whole billion dollars. Congrats")
    else:
        print("I don't know that command")
else:
    print("You didin't type correctly.")
