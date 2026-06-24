from Main import ExecInterrupt

print('\nWelcome to hangman!')
validChoice = False
while not validChoice:
    choice = input("Which word selection method would you like (manual or automatic): ").lower()

    if choice == 'manual':
        from getpass import getpass
        word = getpass(prompt="Enter the secret word: ")
        validChoice = True
    elif choice == 'automatic' or choice == 'auto':
        import random
        validLetters = 'abcdefghijklmnopqrstuvwxyz'
        while True:
            word = random.choice(list(open('words.txt'))).strip().lower()
            for letter in word:
                if letter not in validLetters:
                    continue
            break
        validChoice = True
    else:
        print('\nThat is not a valid word selection method, please try again.\n.')



validLetters = 'abcdefghijklmnopqrstuvwxyz'
solved = False
guessList = []
lives = 6

while not solved:
    print('Here is what your word looks like:')
    for letter in word:
        if letter in guessList:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print(' ')
    if guessList:
        print('You have already guessed', end=' ')
        for letter in guessList:
            print(letter, end=' ')
        print(' ')

    if lives != 1:
        guess = str(input('You have ' + str(lives) + ' lives left. What letter would you like to guess? ')).lower()
    else:
        guess = str(input('You have 1 life left. What letter would you like to guess? ')).lower()

    print('\n')
    if len(guess) != 1:
        print('You must enter a single letter. Please try again.')
        continue
    elif guess not in validLetters:
        print('Sorry, that is not a valid letter. Please try again.')
        continue
    elif guess in guessList:
        print('You have already guessed ' + guess + '. Please try again.')
        continue

    guessList.append(guess)

    for letter in word:
        if letter not in guessList:
            solved = False
            break
        solved = True

    if guess in word:
        print("Yes, '" + guess + "' is in the word.")
    else:
        lives = lives - 1
        if lives == 0:
            print("Sorry, '" + guess + "' is not in the word, and you have run out of lives. The word was '" + word + "'.")
            raise ExecInterrupt
        else:
            print("Sorry, '" + guess + "' is not in the word. Please try again.")

print("Congratulations, you guessed the word! The word was '" + word +"'.")