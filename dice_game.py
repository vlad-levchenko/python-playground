import random


def rollDice():
    diceTotal = random.randint(1, 6) + random.randint(1, 6)
    return diceTotal

def main():
    player1 = input('Enter player 1\'s name:\n')
    player2 = input('Enter player 2\'s name:\n')

    roll1 = rollDice()
    roll2 = rollDice()

    print(player2, 'rolled', roll2)
    print(player1, 'rolled', roll1)

    if roll1 > roll2:
        print(player1, 'wins!')
    elif roll2 > roll1:
        print(player2, 'wins!')
    else:
        print('You tie!')


main()
