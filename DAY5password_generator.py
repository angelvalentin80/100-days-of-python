import string
import random

# my solution
print(string.ascii_uppercase)
print(string.punctuation)

letters_length = int(input("How many letters would you like in your password?\n"))
symbols_length = int(input("How many symbols would you like?\n"))
numbers_length = int(input("How many numbers would you like?\n"))

password_list = []

# random letter
for i in range(0, letters_length):
    random_letter = random.choice(string.ascii_uppercase)
    password_list.append(random_letter)
#symbols
for i in range(0, symbols_length):
    random_symbol = random.choice(string.punctuation)
    password_list.append(random_symbol)
#number
for i in range(0, numbers_length):
    random_number = random.randint(0,9)
    password_list.append(random_number)

password = []

for i in range(0, len(password_list)):
    random_choice = random.choice(password_list)
    password.append(str(random_choice))
    password_list.remove(random_choice)

final_password = ''.join(password)
print(f"Here is your password: {final_password}")
