#Imports
import random
import time

#Background variables
rollCounter = 1
choiceStorage = []
# upperHands = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes"]
# upperScores = ["sum1","sum2","sum3","sum4","sum5","sum6"]
# lowerHands = ["Three of a Kind", "Four of a Kind", "Full House", "Small Straight", "Large Straight", "Yahtzee", "Chance"]
# lowerScores = ["sum","sum","sum",25,30,40,50]
playedScores = []
scoreLog = ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ']
validSmallStraights = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
validLargeStraights = [[1,2,3,4,5],[2,3,4,5,6]]
validDice = 'abcde'
validDiceArray = ['a','b','c','d','e']
validDiceInts = [1,2,3,4,5]
bonusScore = '-'

#Functions
def text_break():
    time.sleep(3)

def dice_convert(string):
    for i in range(0, len(validDiceArray)):
        if string == validDiceArray[i]:
            return validDiceInts[i]
    else:
        return 'error'

def roll(storage, choices):
    for choice in choices:
        storage[choice-1] = random.randint(1,6)

def show_dice():
    print("  A         B         C         D         E  ")
    print("-----     -----     -----     -----     -----")
    print(f"| {dieFaces[0]} |     | {dieFaces[1]} |     | {dieFaces[2]} |     | {dieFaces[3]} |     | {dieFaces[4]} |")
    print("-----     -----     -----     -----     -----")

def show_scorepad():
    print("Upper Section              Lower Section")
    #print("- - - - - - - - - - - - - - - - - - - - - - - ")
    print(f"U1. Aces           |  {scoreLog[0]}{' '*(4-len(str(scoreLog[0])))}| L1. Three of a Kind |  {scoreLog[6]}{' '*(4-len(str(scoreLog[6])))}|")
    print(f"U2. Twos           |  {scoreLog[1]}{' '*(4-len(str(scoreLog[1])))}| L2. Four of a Kind  |  {scoreLog[7]}{' '*(4-len(str(scoreLog[7])))}|")
    print(f"U3. Threes         |  {scoreLog[2]}{' '*(4-len(str(scoreLog[2])))}| L3. Small Straight  |  {scoreLog[8]}{' '*(4-len(str(scoreLog[8])))}|")
    print(f"U4. Fours          |  {scoreLog[3]}{' '*(4-len(str(scoreLog[3])))}| L4. Large Straight  |  {scoreLog[9]}{' '*(4-len(str(scoreLog[9])))}|")
    print(f"U5. Fives          |  {scoreLog[4]}{' '*(4-len(str(scoreLog[4])))}| L5. Full House      |  {scoreLog[10]}{' '*(4-len(str(scoreLog[10])))}|")
    print(f"U6. Sixes          |  {scoreLog[5]}{' '*(4-len(str(scoreLog[5])))}| L6. Yahtzee         |  {scoreLog[11]}{' '*(4-len(str(scoreLog[11])))}|")
    print(f"-------Bonus-------|  {bonusScore}{' '*(4-len(str(bonusScore)))}| L7. Chance          |  {scoreLog[12]}{' '*(4-len(str(scoreLog[12])))}|")

def add_score(category, selection):
    if category == "U" or category == "u":
        total = 0
        match selection:
            case 1:
                for die in dieFaces:
                    if die == 1:
                        total += 1
                playedScores.append(0)
                scoreLog[0] = total
            case 2:
                for die in dieFaces:
                    if die == 2:
                        total += 2
                playedScores.append(1)
                scoreLog[1] = total
            case 3:
                for die in dieFaces:
                    if die == 3:
                        total += 3
                playedScores.append(2)
                scoreLog[2] = total
            case 4:
                for die in dieFaces:
                    if die == 4:
                        total += 4
                playedScores.append(3)
                scoreLog[3] = total
            case 5:
                for die in dieFaces:
                    if die == 5:
                        total += 5
                playedScores.append(4)
                scoreLog[4] = total
            case 6:
                for die in dieFaces:
                    if die == 6:
                        total += 6
                playedScores.append(5)
                scoreLog[5] = total
    else:
        total = 0
        flag = False
        match selection:
            case 1:
                for i in range(1,7):
                    if dieFaces.count(i) >= 3:
                        flag = True
                if flag:
                    for die in dieFaces:
                        total += die
                playedScores.append(6)
                scoreLog[6] = total
            case 2:
                for i in range(1,7):
                    if dieFaces.count(i) >= 4:
                        flag = True
                if flag:
                    for die in dieFaces:
                        total += die
                playedScores.append(7)
                scoreLog[7] = total
            case 3:
                for straight in validSmallStraights:
                    if straight[0] in dieFaces and straight[1] in dieFaces and straight[2] in dieFaces and straight[3] in dieFaces:
                        flag = True
                if flag:
                    scoreLog[8] = 30
                else:
                    scoreLog[8] = 0
                playedScores.append(8)
            case 4:
                for straight in validLargeStraights:
                    if straight[0] in dieFaces and straight[1] in dieFaces and straight[2] in dieFaces and straight[3] in dieFaces and straight[4] in dieFaces:
                        flag = True
                if flag:
                    scoreLog[9] = 40
                else:
                    scoreLog[9] = 0
                playedScores.append(9)
            case 5:
                for i in range(1,7):
                    if dieFaces.count(i) >= 3:
                        for j in range(1,7):
                            if j == i:
                                continue
                            if dieFaces.count(j) >= 2:
                                flag = True
                if flag:
                    scoreLog[10] = 25
                else:
                    scoreLog[10] = 0
                playedScores.append(10)
            case 6:
                for i in range(1, 7):
                    if dieFaces.count(i) >= 5:
                        flag = True
                if flag:
                    scoreLog[11] = 50
                else:
                    scoreLog[11] = 0
                playedScores.append(11)
            case 7:
                for die in dieFaces:
                    total += die
                playedScores.append(12)
                scoreLog[12] = total

def get_number(line):
    return line.split()[1]

print("Welcome to Yahtzee!")

while True:
    rulesCheck = input("Would you like to learn how to play? (y/n) ").lower()
    if rulesCheck == "y":
        print("Yahtzee is a game of dice, where you try to fill up your scoreboard with the highest amount of points possible.")
        text_break()
        print("You will start with a roll of five dice, labelled A B C D and E. ")
        text_break()
        print("You have up to two chances to reroll as many of those dice as you'd like, by entering their letter values.")
        text_break()
        print("If you wish to stop rerolling early, simply hit enter instead of entering any letters.")
        text_break()
        print("Afterwards, you will be shown your scorecard, where you can enter your roll by inputting the score code, which is an alphanumeric code between U1 and L7.")
        text_break()
        print("Each slot in the scorecard can only be used once, so be careful in your selections!")
        text_break()
        print("If you get a total score of 63 or more on the Upper Section, you will automatically unlock a bonus, scoring you an additional 35 points.")
        text_break()
        print("Now it's time to get started, have fun!")
        text_break()
        break
    elif rulesCheck == "n":
        print("Alright, beginning the game now!")
        break
    else:
        print("Please enter a valid input.")

while len(playedScores) < 13:
    choiceStorage = []
    print("\nHere is your starting roll:")
    dieFaces = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    show_dice()

    diceChoices = '0'

    while diceChoices != '':
        diceValid = False
        while not diceValid:
            flag = False
            diceChoices = input("Which dice would you like to reroll? (Enter all letters selected) ").lower()
            if diceChoices == "":
                diceValid = True
                continue

            for die in diceChoices:
                if die not in validDice:
                    print("Sorry, the dice value(s) entered are invalid, please try again.")
                    flag = True
                    break

            if flag:
                continue

            for die in diceChoices:
                choiceStorage.append(dice_convert(die))
            diceValid = True

        if diceChoices == "":
            continue

        roll(dieFaces,choiceStorage)
        print("\nHere is what your dice look like after your second roll:")
        show_dice()

        choiceStorage = []
        diceValid = False
        while not diceValid:
            flag = False
            diceChoices = input("Which dice would you like to reroll? ")
            if diceChoices == "":
                diceValid = True
                continue
            for die in diceChoices:
                if die not in validDice:
                    print("Sorry, the dice value(s) entered are invalid, please try again.")
                    flag = True
                    break
            if flag:
                continue
            for die in diceChoices:
                choiceStorage.append(dice_convert(die))
                diceValid = True

        roll(dieFaces, choiceStorage)
        break
    print("\nHere is what your dice look like after your final roll:")
    show_dice()
    time.sleep(1)
    show_scorepad()
    validScore = False
    while not validScore:
        scoreSelection = input("Where would you like to enter the roll? (enter its code between U1 and L7) ")

        if scoreSelection[:1] == "U" or scoreSelection[:1] == "u":
            if int(scoreSelection[1:])-1 in playedScores:
                print("This score was already played, please try again.")
                continue
            elif scoreSelection[1:] not in ['1','2','3','4','5','6']:
                print("Sorry, the code entered is invalid, please try again.")
                continue
            else:
                validScore = True
        elif scoreSelection[:1] == "L" or scoreSelection[:1] == "l":
            if int(scoreSelection[1:])+5 in playedScores:
                print("This score was already played, please try again.")
                continue
            elif scoreSelection[1:] not in ['1','2','3','4','5','6','7']:
                print("Sorry, the code entered is invalid, please try again.")
                continue
            else:
                validScore = True
        else:
            print("Please enter a valid score code between U1 and L7.")
            continue

        add_score(scoreSelection[:1], int(scoreSelection[1:]))

    bonusCheck = 0
    for i in range(0,6):
        if i in playedScores:
            bonusCheck += scoreLog[i]
    if bonusCheck >= 63:
        bonusScore = 35
    print("\nHere is what your scoresheet looks like now:")
    show_scorepad()

totalScore = 0
for score in scoreLog:
    totalScore += score

if bonusScore == 35:
    totalScore += 35
time.sleep(1)
print("Congratulations on playing Yahtzee! Your final score is: "+str(totalScore)+". ")

#Leaderboard addition
while True:
    name = input("Please enter your name to be added to the leaderboard (1 word only): ")
    if name == "":
        print("Sorry, the name entered is invalid, please try again.")
    else:
        words = name.split(' ')
        if len(words) > 1:
            print('Please enter only one word.')
            continue
        break
writing = '\n'+name + " " + totalScore

with open("yahtzeeScores.txt", 'a') as file:
    file.write(writing)

with open("yahtzeeScores.txt", 'r') as file:
    text = file.read()
    lines = text.splitlines()

    sorted_lines=sorted(lines, key=get_number,reverse=True)

    print('Here are the top five scores on the leaderboard:')
    if len(sorted_lines) >= 5:
        for i in range(0, 5):
            print(str(i + 1) + '. ' + sorted_lines[i])
    else:
        for i in range(0, len(sorted_lines)):
            print(str(i + 1) + '. ' + sorted_lines[i])
