# my solution
people_in_auction = []  # empty dictionary that we will have to add into once we retrieve information

def save_auction_details(name = str, bid = int):
    people_in_auction.append({"name": name, "bid": bid}) 

def check_highest_bid():
    highest_bid = 0
    for i in people_in_auction:
        bid = i["bid"]
        if bid > highest_bid:
            highest_bid = bid
    return highest_bid



auction_ongoing = True

while auction_ongoing:

    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    question = input("Are there any other bidders? Type 'yes' or 'no'.")
   
    save_auction_details(name, bid)

    if question.lower() == "yes":
        continue
    elif question.lower() == "no":
        highest_bid = check_highest_bid()
        print(f"The winner is {name.capitalize()} with a bid of {highest_bid}")  
        auction_ongoing = False
    else:
        print("I don't know that command. You just broke me :(")
