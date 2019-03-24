players = [input('Enter player 1 name'), input('Enter player 2 name')]
x1 = x2 = 0

x1 = input('\n' + players[0] + '\nEnter 1 for rock, \n2 for paper, or \n3 for scissors: ')
x2 = input('\n' + players[1] + '\nEnter 1 for rock, \n2 for paper, or \n3 for scissors: ')

while True:
    while x1 == x2:
        print('Tie! lets go again')
        x1 = input('\n' + players[0] + '\nEnter 1 for rock, \n2 for paper, or \n3 for scissors: ')
        x2 = input('\n' + players[1] + '\nEnter 1 for rock, \n2 for paper, or \n3 for scissors: ')
    #determine winner, then


    playAgain = input('Enter any key to play again, or (q) to quit')
    if (playAgain == 'q' or playAgain == 'Q'): break
print('Thank you for playing!\nCode by Steven \u00a9 2019 All rights reserved')
