
# my solution
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill?")
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15?")
number_of_people = input("How many people to split the bill?")

tip = float(total_bill) * (float(percentage_tip) / 100)
total = float(total_bill) + tip
split = total / float(number_of_people)
print(f"Each person should pay: ${round(split, 2)}")



# extra stuff
# formatting strings with f

score = 0
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, and the statement that you are winning is {isWinning}")
