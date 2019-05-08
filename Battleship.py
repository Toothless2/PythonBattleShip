from random import randint
import os
import time

board = []
ship1_down = 0
ship2_down = 0
double_ship = 0

print("This a simple one player battleship game.")
print("Their are 3 ships. There could be a double length ship too!!")
print("You must destroy the ships in 10 turns.")
print("Each turn you must guess the row and column that you want to fire at")
print("O = The Sea")
print("X = Miss")
print("S = Ship")
print("Press enter to continue.")
input()
os.system('CLS')

#makes the board
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
print("Turn: 1")
print_board(board)

#sets the row the battleships wil be on
def random_row(board):
    return randint(0, len(board) - 1)

#sets the row the battleships wil be on
def random_col(board):
    return randint(0, len(board[0]) - 1)

def random_placement():
    return randint(0, 1)

placer_one = random_placement()
placer_two = random_placement()

ship1_row = random_row(board)
ship1_col = random_col(board)

ship2_row = random_row(board)
ship2_col = random_col(board)

double_ship_source_row = random_row(board)
double_ship_source_col = random_col(board)
double_ship_half_row = double_ship_source_row
double_ship_half_col = double_ship_source_col

#checks if ship 1 and 2 are in the same place
if ship2_row == ship1_row and ship2_col == ship1_col:
    if ship2_row >= 0 and ship2_row < 3:
        ship2_row += 1
    elif ship2_row > 1 and ship2_row >= 3:
        ship2_row = ship2_row - 1

#checks if the source block is overlapping either ship1 or ship2
if (double_ship_source_row == (ship1_row or ship2_row)) and (double_ship_source_col == (ship1_col or ship2_col)):
    if double_ship_source_row <= 2:
        double_ship_source_row += 2
        double_ship_half_row = double_ship_source_row
    elif double_ship_source_row >= 3:
        double_ship_source_row -= 2
        double_ship_half_row = double_ship_source_row

#print(placer_one)
#print(placer_two)

#places second half of the double ship
if placer_one == 0:
    if placer_two == 0:
        if ((double_ship_source_row - 1) != 0) and ((double_ship_source_row - 1) != ship1_row or ship2_row):
            double_ship_half_row = double_ship_source_row - 1
        elif ((double_ship_source_row + 1) != 4) and (double_ship_source_row + 1) != ship1_row or ship2_row:
            second_half_row = double_ship_source_row + 1
        elif ((double_ship_source_col + 1) != 4) and ((double_ship_source_col + 1) != ship1_col or ship2_col):
                double_ship_half_col = double_ship_source_col + 1
        elif (double_ship_source_col - 1) != 0 and ((double_ship_source_col - 1) != ship1_col or ship2_col):
            double_ship_half_col = double_ship_source_col - 1
    elif placer_two == 1:
        if ((double_ship_source_row + 1) != 4) and ((double_ship_source_row + 1) != ship1_row or ship2_row):
            double_ship_half_row = double_ship_source_row + 1
        elif ((double_ship_source_row - 1) != 0) and (double_ship_source_row - 1) != ship1_row or ship2_row:
            second_half_row = double_ship_source_row - 1
        elif ((double_ship_source_col + 1) != 4) and ((double_ship_source_col + 1) != ship1_col or ship2_col):
            double_ship_half_col = double_ship_source_col + 1
        elif (double_ship_source_col - 1) != 0 and ((double_ship_source_col - 1) != ship1_col or ship2_col):
            double_ship_half_col = double_ship_source_col - 1
if placer_one == 1:
    if placer_two == 0:
        if ((double_ship_source_col - 1) != 0) and ((double_ship_source_col - 1) != ship1_col or ship2_col):
            double_ship_half_col = double_ship_source_col - 1
        elif ((double_ship_source_col + 1) != 4) and ((double_ship_source_col + 1) != ship1_col or ship2_col):
            second_half_col = double_ship_source_col + 1
        elif ((double_ship_source_row + 1) != 4) and ((double_ship_source_row + 1) != ship1_row or ship2_row):
            double_ship_half_row = double_ship_source_row + 1
        elif (double_ship_source_row - 1) != 0 and ((double_ship_source_row - 1) != ship1_col or ship2_row):
            double_ship_half_row = double_ship_source_row - 1
    if placer_two == 1:
        if ((double_ship_source_col + 1) != 0) and ((double_ship_source_col + 1) != ship1_col or ship2_col):
            double_ship_half_col = double_ship_source_col + 1
        elif ((double_ship_source_col - 1) != 4) and ((double_ship_source_col - 1) != ship1_col or ship2_col):
            second_half_col = double_ship_source_col - 1
        elif ((double_ship_source_row + 1) != 4) and ((double_ship_source_row + 1) != ship1_row or ship2_row):
            double_ship_half_row = double_ship_source_row + 1
        elif (double_ship_source_row - 1) != 0 and ((double_ship_source_row - 1) != ship1_col or ship2_row):
            double_ship_half_row = double_ship_source_row - 1

#print pos of ships
'''
print("ship 1: Row: " + str(ship1_row) + " Col: " + str(ship1_col))
print("ship 2: Row: " + str(ship2_row) + " Col: " + str(ship2_col))
print("double ship: Row: " + str(double_ship_source_row) + " Col: " + str(double_ship_half_col))
print("double ship pt 2: Row: " + str(double_ship_half_row) + " Col: " + str(double_ship_half_col))
'''

#game logic
for turn in range(10):
    print("Enter a value between 1-5")
    guess_row = input("Row:")
    guess_col = input("Col:")
    
    guess_row = int(guess_row)
    guess_col = int(guess_col)
    
    guess_row = guess_row - 1
    guess_col = guess_col - 1
    
    if guess_row == ship1_row and guess_col == ship1_col:
            ship1_down = 1
            print("You Hit a ship!")
            board[guess_row][guess_col] = "S"
            
            if ship1_down == 1 and ship2_down == 1 and double_ship == 2:
                print("Congrats! You won all the things!")
                time.sleep(5)
                break            
    elif guess_row == ship2_row and guess_col == ship2_col:
        ship2_down = 1       
        print("You Hit a ship!")
        board[guess_row][guess_col] = "S"
        
        if ship1_down == 1 and ship2_down == 1 and double_ship == 2:
            print("Congrats! You won all the things!")
            time.sleep(5)
            break        
    elif guess_row == (double_ship_source_row and double_ship_half_row) and guess_col == (double_ship_source_col and double_ship_half_col):
        double_ship = 2
        print("You hit a ship")
        board[guess_row][guess_col] = "S"
        
        if ship1_down == 1 and ship2_down == 1 and double_ship == 2:
            print("Congrats! You won all the things!")
            time.sleep(5)
            break        
    elif guess_row == double_ship_source_row and guess_col == double_ship_source_col:
        double_ship += 1
        print("You Hit part of a ship!")
        board[guess_row][guess_col] = "S"
        
        if ship1_down == 1 and ship2_down == 1 and double_ship == 2:
            print("Congrats! You won all the things!")
            time.sleep(5)
            break        
    elif guess_row == double_ship_half_row and guess_col == double_ship_source_col:
        double_ship += 1
        print("You Hit part of a ship!")
        board[guess_row][guess_col] = "S"
        
        if ship1_down == 1 and ship2_down == 1 and double_ship == 2:
            print("Congrats! You won all the things!")
            time.sleep(5)
            break        
    elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print("Oops, that's not even in the ocean.")
    elif(board[guess_row][guess_col] == "X"):
        print("You guessed that one already.")
    elif turn == 9:
        print("Game Over!")
        time.sleep(5)
        break
    else:
        print("You missed my battleship!")    
        board[guess_row][guess_col] = "X"
    time.sleep(1)
    os.system('CLS')
    turn = turn + 2
    print("Turn: " + str(turn))
    print_board(board)