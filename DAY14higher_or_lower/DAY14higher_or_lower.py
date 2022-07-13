# my solution
import random
from game_data import data 

score = 0

def get_random_person() -> dict:
    """This is going to be grabbing a random person from the data and returning them"""
    person = random.choice(data)
    return person

def calculate_same_followers(p1 = dict, p2 = dict):
    """this is going to check if the people have the same follower count. If so we are going to assign a new person. """
    if p1['follower_count'] == p2['follower_count']:
        substitute = get_random_person()
        return substitute 
    else:
        return p1

def comparison_statement(person = dict):
    """This is the print statement where we announce the person and describe that person"""
    name = person['name']
    description = person['description']
    country = person['country']
    return f"{name.title()}, a {description}, from {country.title()}"

def calculate_winner(person1, person2):
    """Calculate who has the most amount of followers and return that person"""
    person1_followers = person1['follower_count']
    person2_followers = person2['follower_count']
    
    if person1_followers > person2_followers:
        return "a"
    elif person2_followers > person1_followers:
        return "b"

game_on = True
while game_on:
    famous_person1 = get_random_person()  
    famous_person2 = get_random_person() 
    
    famous_person1 = calculate_same_followers(famous_person1, famous_person2)
    

    print(f"Compare A: {comparison_statement(famous_person1)}")

    print("\n\nVS\n\n")

    print(f"Against B: {comparison_statement(famous_person2)}")
    choice = input("Who has more followers? Type 'A' or 'B': ")
    winner = calculate_winner(famous_person1, famous_person2)

    if choice.lower() == winner.lower():
        score += 1
        print(f"You're right! Current score: {score}\n") 
        continue
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_on = False



