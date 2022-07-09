
# my solution
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?"))
percentage_tip = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
number_of_people = int(input("How many people to split the bill?"))

tip = total_bill * (percentage_tip / 100)
total = total_bill + tip
split = total / number_of_people
rounded_amount = round(split, 2)

# formatting
final_amount = "{:.2f}".format(rounded_amount) #turning this into a string that is formatted.
print(f"Each person should pay: ${final_amount}")



# extra stuff
# formatting strings with f

score = 0
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, and the statement that you are winning is {isWinning}")
