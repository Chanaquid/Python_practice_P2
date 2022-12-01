import random
import os 
choices = ['rock', 'paper', 'sissor']
status = True

while status:
    player = (input("Please type (rock, paper or sissor): ").lower())
    Computer = choices[random.randint(0,2)]
    print('Computer played: {0}!'.format(Computer))

    # Draw 
    if (player == Computer):
        print('Equal! Please try again')
    
    # Paper beats rock
    elif(player == choices[1] and Computer == choices[0]):
        print('You Won!!')

    # Rock beats Sissor
    elif(player == choices[0] and Computer == choices[2]):
        print('You Won!!')
    
    # Sissors beat paper
    elif (player == choices[2] and Computer == choices[1]):
        print('You Won!!')
    
    # if the input is invalid
    elif (player != choices):
        print('Invalid Input, Please type (rock, paper or sissor):')
    
    # if any other result from above computer Wins
    else:
        print('Computer Won!! Please Try Again!!')

    check = input("Would you like to play again? (y / n) ")
    if (check == 'y'):
        continue
    else:
        status = False

os.system('cls')
