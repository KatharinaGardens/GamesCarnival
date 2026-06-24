
class ExecInterrupt(Exception):
    pass

import time

def show_games():
    print("1. Hangman")
    print("2. Tic-Tac-Toe")
    print("3. Yahtzee")
    print("E. Exit")

def main():
    print("Welcome to the game center!")

    while True:
        show_games()
        choice = input("Please insert the number of the game you would like to play. ")

        match choice:
            case '1':
                try:
                    exec(open("Hangman.py").read())
                except ExecInterrupt:
                    pass
                time.sleep(1)
                print("\nWelcome back to the game center!")
            case '2':
                try:
                    exec(open("Tic-Tac-Toe.py").read())
                except ExecInterrupt:
                    pass
                time.sleep(1)
                print("\nWelcome back to the game center!")
            case '3':
                try:
                    exec(open("Yahtzee.py").read())
                except ExecInterrupt:
                    pass
                time.sleep(1)
                print("\nWelcome back to the game center!")
            case 'E'|'e':
                print("Thank you for playing. See you next time!")
                exit(0)
            case _:
                print("Sorry, I didn't understand that. Please try again.")


if __name__ == '__main__':
    main()