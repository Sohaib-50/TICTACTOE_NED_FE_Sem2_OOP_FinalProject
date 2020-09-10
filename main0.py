import tictactoe4 as ttt
from sys import exit
import pprint

X = 'X'
O = 'O'
EMPTY = None

## Top messages

continue_playing = True
while continue_playing:
    game = ttt.Game()
    game.play()
    print()
    if play_again := input("Do you want to play again?[y/Y]: ").upper() != 'Y':
        print("Closing game...")
        exit(0)

#TODO Run and make consistent
    





