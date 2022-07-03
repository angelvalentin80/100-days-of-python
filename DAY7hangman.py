import random

word_list = ["tacosalpastor", "ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat",
             "clam", "cobra", "cougar", "coyote", "crow", "deer", "dog", "donkey", "duck", "eagle", "ferret",
             "fox", "frog", "goat", "goose", "hawk", "lion", "lizard", "llama", "mole", "monkey", "moose",
             "mouse", "mule", "newt", "otter", "owl", "panda", "parrot", "pigeon", "python", "rabbit", "ram",
             "rat", "raven", "rhino", "salmon", "seal", "shark", "sheep", "skunk", "sloth", "snake", "spider",
             "stork", "swan", "tiger", "toad", "trout", "turkey", "turtle", "weasel", "whale", "wolf",
             "wombat", "zebra"]

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# WORD
for word in word_list:
    word = random.choice(word_list)

#word = word_list[0]
word_as_list = []

for i in word:
    letter = i.lower()
    word_as_list.append(letter)
# word

# underlines
word_to_guess = []
for i in word:
    if i == " ":
        word_to_guess.append(' ')
    else:
        word_to_guess.append('_')
word_in_underlines = ' '.join(word_to_guess)
#underlines


game_over = False
score = 6  # user has 6 tries. Once 0 we lose the game
index_increment = 0
previous_letters = []
while game_over == False:
    # game start

    letter = input("Guess a letter: ")
    print("\n")

    for i in word_as_list:
        if letter.lower() == i:
            word_to_guess[index_increment] = letter
            word_in_underlines = ' '.join(word_to_guess)
        index_increment += 1

    if letter.lower() not in word_as_list:
        score -= 1
        print(f"You guessed {letter} that's not in the word. You lose a life.")

    if letter.lower() in previous_letters:
        print("You already guessed that letter!")



    print(word_in_underlines + "\n")

    if word_to_guess == word_as_list:
        print(f"You Win! The word was {word}")
        game_over = True
    
    # score keeper
    if score == 6:
        print(HANGMANPICS[0])
    elif score == 5:
        print(HANGMANPICS[1])
    elif score == 4:
        print(HANGMANPICS[2])
    elif score == 3:
        print(HANGMANPICS[3])
    elif score == 2:
        print(HANGMANPICS[4])
    elif score == 1:
        print(HANGMANPICS[5])
    else:
        print(HANGMANPICS[6])
        print("You lose")
        game_over = True


    index_increment = 0
    previous_letters.append(letter)
