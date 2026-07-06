#imports
import time
from unittest import case

from termcolor import cprint
import random

#Functions
def line_break():
    time.sleep(2)

def little_line_break():
    time.sleep(1)

def clear_screen():
    print('\n' * 25)

color_dict = {
    0: 'Pink',
    1: 'Red',
    2: 'Orange',
    3: 'Yellow',
    4: 'Green',
    5: 'Blue',
    6: 'White',
    7: 'Silver'
}

reverse_color_dict = {
    'pink' : 0,
    'red' : 1,
    'orange' : 2 ,
    'yellow' : 3,
    'green' : 4,
    'blue' : 5,
    'white' : 6,
    'silver': 7
}

intro_rule_list = [
    '\nMastermind is a game where you attempt to guess what colors are in a hidden sequence.',
    'The computer or a friend will hide a sequence of four colors for you to guess.',
    'Each color in the sequence can be any color in the eight available options: '
]

color_rule_list = [
    ('Pink', 'magenta'),
    ('Red', 'red'),
    ('Orange', (255,165,0)),
    ('Yellow', (255,222,33)),
    ('Green', 'green'),
    ('Blue', 'blue'),
    ('White', (255,255,255)),
    ('Silver', 'light_grey')
]

outro_rule_list = [
    'After the hidden sequence is made, you can begin guessing!',
    'You have 12 guesses to correctly identify the hidden sequence.',
    'Each time you make a guess, you will be given two scores: ',
    'One for how many colors that are correct and in the correct position,',
    'And one for how many colors that are correct but not in the correct position.',
    "Now let's start the game!\n"
]

def show_colors():
    for line in color_rule_list:
        cprint(*line)
        little_line_break()

def show_color_list():
    print('Here are the available colors:')
    for line in color_rule_list:
        cprint(*line, end = ' ')

def show_rules():
    for line in intro_rule_list:
        print(line)
        line_break()

    show_colors()
    line_break()

    for line in outro_rule_list:
        print(line)
        line_break()


def intro_rules():
    while True:
        rules = input('Would you like to hear the rules of the game? (y/n) ').lower()

        match rules:
            case 'y':
                show_rules()
                break
            case 'n':
                print("Okay, let's start the game!")
                break
            case _:
                print('Invalid input, please try again.')

def select_game_mode():
    print('\nHere are the game modes:')
    print('1. Random Mode - Play a random seed set up by the computer!')
    print('2. Set seed mode - Give the computer to your friend and let them enter a setup!')
    print('3. VS Mode - Play a game against your friend')

    while True:
        mode = input('Enter your choice of game mode: ').lower()

        match mode:
            case '1':
                return 1
            case '2':
                return 2
            case '3':
                return 3
            case _:
                print('The choice you entered was invalid. Please try again.')

def select_repetition_mode():
    while True:
        print('\nWould you like to allow for colors to be repeated within a clue?')
        print('1. Yes')
        print('2. No')
        choice = input('Enter your choice: ').lower()

        match choice:
            case '1':
                return True
            case '2':
                return False
            case _:
                print('The choice you entered was invalid. Please try again.')

def select_code_mode():
    while True:
        print('\nWould you like to enter the length of the secret code?')
        print('1. Yes')
        print('2. No, let my friend decide how long to make the code.')
        choice = input('Enter your choice: ').lower()
        match choice:
            case '1':
                return True
            case '2':
                return False
            case _:
                print('The choice you entered was invalid. Please try again.')

def select_secret_code_length():
    while True:
        print('\nHow long would you like the secret code to be?')
        print('The standard game uses a length of 4.')
        secret_code_length = input('Enter your secret code length: ').lower()

        try:
            secret_code_length = int(secret_code_length)
        except ValueError:
            print('The secret code length you entered was invalid. Please try again.')
        else:
            if secret_code_length < 1:
                print('The secret code length you entered was too short. Please try again.')
            else:
                return secret_code_length

def select_vs_mode():
    while True:
        print('\nWould you like to play with the same computer generated secret code?')
        print('1. Yes, let the computer generate a secret code.')
        print('2. No, we\'d like to each make a code for each other.')
        choice = input('Enter your choice: ').lower()

        match choice:
            case '1':
                return True
            case '2':
                return False
            case _:
                print('The choice you entered was invalid. Please try again.')

def generate_secret_code(repetition_flag, code_length):
    if repetition_flag:
        secret_code = [random.randint(0, 7) for i in range(code_length)]
    else:
        secret_code = random.sample([0, 1, 2, 3, 4, 5, 6, 7],k=code_length)

    return secret_code


def validate_secret_code(repetition_flag, code_length):
    while True:
        color_choices = input('\nEnter the color(s) you want to choose, separated by a space. ').lower()
        flag = False
        secret_code = []

        if color_choices == 'show colors' or color_choices == 'c':
            show_color_list()
            flag = True
        else:
            for color in color_choices.split():
                try:
                    secret_code.append(reverse_color_dict[color])
                except KeyError:
                    print('The color you entered was invalid or couldn\'t be understood. Please try again.')
                    print('If you would like to see the list of available colors, type "show colors" or "c".')
                    flag = True
                    continue
            if len(secret_code) == 0:
                print('Please enter at least one color.')
                flag = True
            if code_length:
                if secret_code != code_length:
                    print(f'Please enter a code of length {code_length}.')
                    flag = True
            if not repetition_flag:
                for i in range(len(secret_code)):
                    for j in range(i+1,len(secret_code)):
                        if secret_code[i] == secret_code[j]:
                            flag = True
                            print('Color repetition is disabled, please try again.')




        if not flag:
            return secret_code, len(secret_code)

def validate_guess(code_length, repetition_flag):
    print('If you would like to see the list of available colors, type "show colors" or "c".')
    while True:
        guess_string = input('\nEnter your guess: ').lower()
        guess = []
        flag = False

        if guess_string == 'show colors' or guess_string == 'c':
            show_color_list()
            flag = True
        else:
            for word in guess_string.split():
                try:
                    guess.append(reverse_color_dict[word])
                except KeyError:
                    print('The guess you entered was invalid. Please try again.')
                    print('If you would like to see the list of available colors, type "show colors" or "c".')
                    flag = True

            if len(guess) != code_length:
                print(f'Your guess should contain {code_length} color{'s' if code_length != 1 else 's'}.')
                flag = True
            if not repetition_flag:
                for i in range(len(guess)):
                    for j in range(i+1,len(guess)):
                        if guess[i] == guess[j]:
                            flag = True

                if flag:
                    print('Color repetition is disabled, please guess again.')

        if not flag:
            return guess


def correct_check(secret_code, guess):
    """ Takes a secret code and a guess and returns the indexes of the correct numbers within the guess"""
    correct_guesses = []

    for i in range(len(guess)):
        if secret_code[i] == guess[i]:
            correct_guesses.append(i)

    return correct_guesses

def position_check(remaining_nums, guess):
    position_guesses = 0
    for int in guess:
        if int in remaining_nums:
            position_guesses += 1
            remaining_nums.remove(int)

    return position_guesses

def play_game(secret_code, repetition_flag):
    print(f'The secret code is {len(secret_code)} color{'s' if len(secret_code) != 1 else ''} long. Good luck!')
    guess_counter = 0
    while True:
        guess = validate_guess(len(secret_code), repetition_flag)
        guess_counter += 1

        if guess == secret_code:
            print('You guessed the secret code!')
            return guess_counter

        correct_guesses = correct_check(secret_code, guess)
        correct_guesses.reverse()

        for i in correct_guesses:
            guess[i] = 9

        remaining_nums = secret_code[:]
        for i in correct_guesses:
            remaining_nums.pop(i)

        position_guesses = position_check(remaining_nums, guess)

        print(f'Your guess contained {len(correct_guesses)} color{'s that were' if len(correct_guesses) != 1 else ' that was'} completely correct, and {position_guesses} color{'s that were' if position_guesses != 1 else ' that was'} correct but in the wrong position.')

print('Welcome to Mastermind!')
intro_rules()
gameChoice = select_game_mode()

match gameChoice:
    case 1:
        repetition_flag = select_repetition_mode()
        code_length = select_secret_code_length()
        print('\nOkay, the computer is deciding where the colors are placed.')

        secret_code = generate_secret_code(repetition_flag,code_length)
        score = play_game(secret_code, repetition_flag)

        print(f'Congratulations, you guessed the secret code in {score} guesses!')


    case 2:
        repetition_flag = select_repetition_mode()
        code_length_flag = select_code_mode()

        if code_length_flag:
            code_length = select_secret_code_length()
        else:
            code_length = None

        print('\nSet seed mode - Give the device to your friend and let them enter a setup!')

        show_color_list()
        secret_code, code_length = validate_secret_code(repetition_flag,code_length)

        clear_screen()
        score = play_game(secret_code, repetition_flag)

        print(f'Congratulations, you guessed the secret code in {score} guess{'es' if score != 1 else ''}!')


    case 3:
        print('\nVS Mode - Play a game against your friend')
        computer_flag = select_vs_mode()
        repetition_flag = select_repetition_mode()
        code_length = select_secret_code_length()

        if computer_flag:
            print('\nOkay, the computer is deciding where the colors are placed.')
            secret_code = generate_secret_code(repetition_flag,code_length)
        else:
            print('\nOkay Player 2, make a secret code for Player 1!')
            secret_code = validate_secret_code(repetition_flag,code_length)

        clear_screen()
        print('Player 1, it\'s your turn!')
        player_1_score = play_game(secret_code, repetition_flag)
        print(f'Congratulations Player 1, you guessed the secret code in {player_1_score} guess{'es' if player_1_score != 1 else ''}!')
        line_break()
        line_break()
        clear_screen()

        if not computer_flag:
            print('\nOkay Player 1, make a secret code for Player 2!')
            secret_code = validate_secret_code(repetition_flag, code_length)
            clear_screen()

        print('Alright, Player 2, it\'s your turn!')
        player_2_score = play_game(secret_code, repetition_flag)
        print(f'Congratulations Player 2, you guessed the secret code in {player_2_score} guess{'es' if player_2_score != 1 else ''}!')
        line_break()
        line_break()

        if player_1_score == player_2_score:
            print('Good job to you both, it\'s a tie!')
        else:
            print(f'\n\n\n\nGood job Player {1 if player_1_score < player_2_score else 2}, you won!')

