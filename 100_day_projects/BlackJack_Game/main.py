from art import logo
import random
import time

def randomCard():
    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(deck)
    return card

card1 = randomCard()
card2 = randomCard()
new_card = randomCard()
dealer_card1 = randomCard()
dealer_card2 = randomCard()
new_dealer_card = randomCard()
game_play = True
user_money = 0

print()
startGame = input("Do you want to play a game of blackjack? y or n\n").lower()
user_money = int(input("How much money do you have to start betting?\n"))
print(logo)

while game_play:
    if startGame == "y":
        print(f"Current betting money: {user_money}")
        bet = int(input("How much would you like to bet?\n"))
        print(f"Your cards are {card1} and {card2}")
        total = card1 + card2

        userChoice = input("Would you like to stay or hit?\n").lower()

        while userChoice == "hit":
            if userChoice == "hit":
                print(f"Your new card is {new_card}")
                total = total + new_card

                if total > 21:
                    print("You BUSTED!")
                    total = 0
                    break
            
            userChoice = input("Would you like to stay or hit?\n").lower()
        
        for x in range(3, 0, -1):
            print("The dealer is going...")
            time.sleep(1)
        print()
        print(f"Dealer's cards are {dealer_card1} and {dealer_card2}")

        dealer_total = dealer_card1 + dealer_card2

        if dealer_total < 15:
            print(f"Dealer chose to hit, dealer got {new_dealer_card}")
            dealer_total = dealer_total + new_dealer_card

        if dealer_total > 21:
            print("Dealer busted")
            dealer_total = 0

        if dealer_total > total:
            print("You Lost!")
            print(f"You lost -{bet}")
            user_money = user_money - bet
        elif dealer_total < total:
            bet = bet * 2
            print("You WON!")
            print(f"You won {bet}")
            user_money = user_money + bet
        elif dealer_total == total:
            print("No one won.")

        if user_money <= 0:
            print("You're out of cash.")
            break

        again = input("Would you like to play again? y or n\n")

        if again == "y":
            card1 = randomCard()
            card2 = randomCard()
            new_card = randomCard()
            dealer_card1 = randomCard()
            dealer_card2 = randomCard()
            new_dealer_card = randomCard()
            game_play = True
        else:
            print("Thanks for playing.")
            game_play = False
            break
    else:
        print("Pussy.")
        break
        
print()

