#Initial Setup
import random
import time

xOwned = []
oOwned = []
spacesFilled = []
board = ['1','2','3','4','5','6','7','8','9']
winCombos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
gameOver = False
turn = 0

def show_board():
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("------------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("------------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def has_won(spaces):
    for winSet in winCombos:
        if winSet[0] in spaces and winSet[1] in spaces and winSet[2] in spaces:
            return True

    return False

def would_win(spaces):
    for i in range(1, 10):
        temp_owned = spaces.copy()

        if i not in spacesFilled:
            temp_owned.append(i)
        else:
            continue

        if has_won(temp_owned):
            store = i
            return [True, store]
    return [False, 0]

print("Welcome to Tic Tac Toe!")
time.sleep(1)

if random.randint(0, 1) == 0:
    print("You will go first, and play the Os. Where would you like to go?")
    turn = 0
else:
    print("I will go first, and play the Xs.")
    turn = 1

while not gameOver:
    while turn == 0:
        show_board()

        choice = input("Please enter the number of the space you would like to fill. ")

        try:
            choice = int(choice)
        except ValueError:
            print("\nNon-valid input received. Please try again.")
            continue

        if choice in spacesFilled:
            print("\nThis space has already been filled.")
            continue

        oOwned.append(choice)
        spacesFilled.append(choice)
        board[choice-1] = 'O'

        print("\nHere is the board after your move:")
        show_board()

        if has_won(oOwned):
            print("You won, congratulations!")
            gameOver = True

        if len(spacesFilled) == 9:
            print("Tie game!")
            gameOver = True
            break

        time.sleep(1.5)
        turn = 1

    if gameOver:
        break

    while turn == 1:

        flag, move = would_win(xOwned)

        if not flag:
            flag, move = would_win(oOwned)

        if not flag:
            validMove = False
            while not validMove:
                move = random.randint(1,9)
                if move not in spacesFilled:
                    validMove = True

        xOwned.append(move)
        spacesFilled.append(move)
        board[move-1] = 'X'

        if has_won(xOwned):
            print("\nHere is the board after my move:")
            show_board()
            print("Sorry, you lost.")
            gameOver = True
            time.sleep(1)
            break

        if len(spacesFilled) == 9:
            print("\nHere is the board after my move:")
            show_board()
            print("Tie game!")
            gameOver = True
            time.sleep(1)
            break

        print("\nHere is the board after my move:")

        turn = 0

print("\nThank you for playing!")