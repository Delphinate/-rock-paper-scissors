import random

# in fact for those who have no friends
print('This program is designed for those who have no one to play with in the rock scissors paper.')
while True:
    try:
        game = int(input('1-Rock 2-Scissors 3-Paper: '))
        game1 = random.randint(1, 3)
        print(f'You have chosen {game} and the program {game1}')
        if game == game1:
            print('Friendship won.')
            continue
        if game == 1 and game1 == 2:
            print('Rock beats scissors.You are winner.')
            continue
        if game == 1 and game1 == 3:
            print('Paper covers Rock.Program is winner.')
            continue
        if game == 2 and game1 == 1:
            print('Rock beats scissors.Program is winner.')
            continue
        if game == 2 and game1 == 3:
            print('Scissors cut paper.You are winner.')
            continue
        if game == 3 and game1 == 1:
            print('Paper covers Rock.You are winner.')
            continue
        if game == 3 and game1 == 2:
            print('Scissors cut paper.Program is winner.')
            continue
        else:
            print('Make the right choice.')
    except ValueError:
        print('We need numbers')
