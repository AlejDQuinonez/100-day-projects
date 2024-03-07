import sys
from Questions import *
from random import randrange
from PIL import Image

print()
print(greeting)
startGame = input("Would you like to play? Type Y or N\n").lower()
print()

if startGame == "y":
    #First Question
    print(Question1)
    print(Answer1A)
    print(Answer1B)
    print(Answer1C)
    print()
    player_answer = input("Answer: ").lower()
    if player_answer == "a" or "b" or "c":
        player_points = randrange(1, 20)
    points = player_points
    print("Current points: " + str(points))

    #Second Question
    print()
    print(Question2)
    print(Answer2A)
    print(Answer2B)
    print(Answer2C)
    print()
    player_answer = input("Answer: ").lower()
    if player_answer == "a" or "b" or "c":
        player_points = randrange(1, 20)
    points += player_points 
    print("Current points: " + str(points))

    #Third Question part 1
    print()
    print(Question3)
    print(Answer3A)
    print(Answer3B)
    print(Answer3C)
    print()
    player_answer = input("Answer: ").lower()
    if player_answer == "a" or "c":
        player_points = randrange(1, 20)
        points += player_points 
        print("Current points: " + str(points))

    if player_answer == "b":
        player_points = randrange(1, 20)
        points += player_points
        #third question part 2
        print()
        print(Question3_1)
        print(Answer3_1A)
        print(Answer3_1B)
        print(Answer3_1C)
        print()
        player_answer = input("Answer: ").lower()
        if player_answer == "b":
            #Third question part 2.2
            print()
            print(Question3_2B)
            print()
            player_number = input("Here: ")
            if player_number != "skip":
                bonus = 100
                points = points + bonus

            if player_number == "skip":
                #Third question part 2.3
                print()
                print(Question3_2B1)
                print()
        elif player_answer == "a" or "c":
            #Third question part 2.1
            print()
            print(Question3_2A)
            player_points = randrange(1, 20)
            points += player_points
    
        print("Current points: " + str(points))
        print()

    #Fourth Question part 1
    print(Question4)
    print(Answer4A)
    print(Answer4B)
    print(Answer4C)
    print()
    player_answer = input("Answer: ").lower()
    if player_answer == "a" or "b":
        player_points = randrange(1, 20)
        points += player_points
        print("Current points: " + str(points))
        print()

    if player_answer == "c":
        player_points = randrange(1, 20)
        points += player_points
        #Fourth Question part 2
        print()
        print(Question4_1)
        print(Answer4A_1)
        print(Answer4B_1)
        print()
        player_answer = input("Answer: ").lower()
        if player_answer == "a" or "b":
            player_points = randrange(1, 20)
            points += player_points
            print("Current points: " + str(points))
            print()

    #fifth Question part 1
    print()
    print(Question5)
    print(Answer5A)
    print(Answer5B)
    print(Answer5C)
    print()
    player_answer = input("Answer: ").lower()
    if player_answer == "a" or "c":
        player_points = randrange(1, 20)
        points += player_points 
        print("Current points: " + str(points))

    if player_answer == "b":
        player_points = randrange(1, 20)
        points += player_points 
        #Fifth Question part 2
        print()
        print(Question5B_1)
        print(Answer5B_1A)
        print(Answer5B_1B)
        print()
        player_answer = input("Answer: ").lower()
        if player_answer == "a" or "b":
            player_points = randrange(1, 20)
            points += player_points 
            print("Current points: " + str(points))
            
    #Sixth Question
    print()
    print(Question6)
    print(Answer6A)
    print(Answer6B)
    print(Answer6C)
    print()
    player_answer = input("Answer: ").lower()
    if player_answer == "a" or "b" or "c":
        player_points = randrange(1, 20)
    points += player_points
    print("Current points: " + str(points))

    #Seventh Question
    print()
    print(Question7)
    print(Answer7A)
    print(Answer7B)
    print(Answer7C)
    print()
    player_answer = input("Answer: ").lower()
    if player_answer == "a" or "b" or "c":
        player_points = randrange(1, 20)
    points += player_points
    print("Current points: " + str(points))

    #Eighth question
    print()
    print(Question8)
    print(Answer8A)
    print(Answer8B)
    print(Answer8C)
    print()
    player_answer = input("Answer: ").lower()
    if player_answer == "a" or "b" or "c":
        player_points = randrange(1, 20)
    points += player_points
    print("Current points: " + str(points))

    #Ninth Question
    print()
    print(Question9)
    print(Answer9A)
    print(Answer9B)
    print(Answer9C)
    print()
    player_answer = input("Answer: ").lower()
    if player_answer == "a" or "b" or "c":
        player_points = randrange(1, 20)
    points += player_points
    print("Current points: " + str(points))

    #Tenth Question
    print()
    print(Question10)
    print(Answer10A)
    print(Answer10B)
    print(Answer10C)
    print()
    player_answer = input("Answer: ").lower()
    if player_answer == "a" or "b" or "c":
        player_points = randrange(1, 20)
    points += player_points
    print("Total points: " + str(points))

    if points >= 250:
        print()
        print("Congratulations your morals are just, here's a picture for your reward!")
        img = Image.open("100_day_projects/Ethics_Game/Pictures/Leonardo-Dicaprio-Cheers.jpeg")
        img.show()
    else:
        print()
        print("Congratulations your morals are fucked!")
else:
    print("I knew you were a pussy. Bye.")
    print()
    sys.exit()
print()