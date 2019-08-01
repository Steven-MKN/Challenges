#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
#print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
#Remember the rules:
#
#Rock beats scissors
#Scissors beats paper
#Paper beats rock

players = [input('Enter player 1 name: '), input('Enter player 2 name: ')]
x1 = x2 = 0

x1 = input('\n' + players[0] + '\nEnter 1 for rock, \n2 for paper, or \n3 for scissors: ')
x2 = input('\n' + players[1] + '\nEnter 1 for rock, \n2 for paper, or \n3 for scissors: ')

while True:
    while x1 == x2:
        print('Tie! lets go again')
        x1 = input('\n' + players[0] + '\nEnter 1 for rock, \n2 for paper, or \n3 for scissors: ')
        x2 = input('\n' + players[1] + '\nEnter 1 for rock, \n2 for paper, or \n3 for scissors: ')

    if ((x1=='1' and x2=='3') or (x1=='2' and x2=='1') or (x1=='3' and x2=='2')): print(players[0] + ' wins, congrats!')        
    else: print(players[1] + ' wins, congrats!')

    playAgain = input('Enter any key to play again, or (q) to quit: ')
    if (playAgain == 'q' or playAgain == 'Q'): break
    x1 = x2
        
print('******************************\nThank you for playing!'
    +'\nCode by Steven \u00a9 2019 All rights reserved')
