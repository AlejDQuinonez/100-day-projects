#HOW TO IMPROVE:
# - Add multiple player lives
# - when a player dies, ask if they want to keep going

from art import *
import random
import sys

print()
print(rules)
print()
startGame = input("Would you like to play Escape? Type 'yes' or 'exit'\n").lower()

#Creates the size of the Grid
width = 10
height = 10
matrix = [[placeHolder for x in range(width)] for y in range(height)]

#Player and Goal starting Positions
player_position_x = 0
player_position_y = 0
matrix[player_position_y][player_position_x] = happy_face

goal_position_x = random.randrange(0,10)
goal_position_y = random.randrange(0,10)
matrix[goal_position_x][goal_position_y] = goal

#Functions that move the player
def right(move_right):
    return 1 + move_right

def left(move_left):
    return move_left - 1

def up(move_up):
    return move_up - 1

def down(move_down):
    return 1 + move_down

if startGame == "exit":
    print()
    print("Good-Bye.")
    print()
    sys.exit()

while startGame == "yes":
    #Randomizes enemy positions (for three enemies)
    enemy_position_x = random.randrange(0,5)
    enemy_position_y = random.randrange(0,5)
    enemy_position_z = random.randrange(0,5)
    matrix[enemy_position_y][enemy_position_z] = random.choice(enemies_list)
    matrix[enemy_position_y][enemy_position_x] = random.choice(enemies_list)
    matrix[enemy_position_x][enemy_position_z] = random.choice(enemies_list)

    #Changes player's position
    matrix[player_position_y][player_position_x] = happy_face

    #Prints Grid
    print()
    print(*matrix, sep = "\n")
    print()

    #Erases player's previous position
    matrix[player_position_y].pop(player_position_x)
    matrix[player_position_y].insert(player_position_x, placeHolder)

    #Erases enemy's previous position
    matrix[enemy_position_y].pop(enemy_position_z)
    matrix[enemy_position_y].insert(enemy_position_z, placeHolder)
    matrix[enemy_position_y].pop(enemy_position_x)
    matrix[enemy_position_y].insert(enemy_position_x, placeHolder)
    matrix[enemy_position_x].pop(enemy_position_z)
    matrix[enemy_position_x].insert(enemy_position_z, placeHolder)

    #Player's decision on where to move
    player_movement = input("Where would you like to move?\n").lower()
    if player_movement == "right":
        player_position_x = right(player_position_x)
    elif player_movement == "left":
        player_position_x = left(player_position_x)
    elif player_movement == "up":
        player_position_y = up(player_position_y)
    elif player_movement == "down":
        player_position_y = down(player_position_y)
    elif player_movement == "exit":
        print()
        print("Quitter.")
        break

    #If player matches same position as enemy, they lose
    if enemy_position_y == player_position_y and enemy_position_z == player_position_x:
        matrix[player_position_y][player_position_x] = dead
        print()
        print(*matrix, sep = "\n")
        print()
        print("YOU DIED.")
        break
    elif enemy_position_z == player_position_y and enemy_position_y == player_position_x:
        matrix[player_position_y][player_position_x] = dead
        print()
        print(*matrix, sep = "\n")
        print()
        print("YOU DIED.")
        break
    elif enemy_position_y == player_position_y and enemy_position_x == player_position_x:
        matrix[player_position_y][player_position_x] = dead
        print()
        print(*matrix, sep = "\n")
        print()
        print("YOU DIED.")
        break
    elif enemy_position_x == player_position_y and enemy_position_y == player_position_x:
        matrix[player_position_y][player_position_x] = dead
        print()
        print(*matrix, sep = "\n")
        print()
        print("YOU DIED.")
        break
    elif enemy_position_z == player_position_y and enemy_position_x == player_position_x:
        matrix[player_position_y][player_position_x] = dead
        print()
        print(*matrix, sep = "\n")
        print()
        print("YOU DIED.")
        break
    elif enemy_position_x == player_position_y and enemy_position_z == player_position_x:
        matrix[player_position_y][player_position_x] = dead
        print()
        print(*matrix, sep = "\n")
        print()
        print("YOU DIED.")
        break

    #If player matches the green sqaure they win
    if matrix[goal_position_x][goal_position_y] == matrix[player_position_y][player_position_x]:
        matrix[goal_position_x][goal_position_y] = party_face
        print()
        print(*matrix, sep = "\n")
        print()
        print("YOU WON!")
        print()
        keep_going = input("Would you like to keep playing? Type 'yes' to keep playing or 'no' to quit.\n").lower()

        #Resets the game
        if keep_going == "yes":
            startGame = keep_going
            goal_position_x = random.randrange(0,10)
            goal_position_y = random.randrange(0,10)
            matrix[goal_position_x][goal_position_y] = goal
        else:
            break

    