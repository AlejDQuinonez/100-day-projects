#HOW TO IMPROVE:
# - add a word pile of already used letters

import random
from art import logo, stages
from word_bank import word_list

#Choses the word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ["_" for space in range(word_length)]
Game = False
Lives = 6

print(logo)
print()
# print(f"The word is {chosen_word}")

while not Game:
    #Displays the empty word and ask user for answer
    print()
    print(f"{''.join(display)}")
    print()
    guess = input("Guess a letter:\n").lower()

    #Checks if the letter is in the word
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    
    #If the letter is not in the word a life is taken
    if guess not in chosen_word:
        print()
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        Lives -= 1
        if Lives == 0:
            print()
            print("You lose.")
            print(f"The word was {chosen_word}")
            print()
            Game = True

    #Checks if the user figured out the word and ends the game
    if "_" not in display:
        print()
        print("You won!")
        print(f"The word was {''.join(display)}")
        print()
        Game = True

    print(stages[Lives])
    