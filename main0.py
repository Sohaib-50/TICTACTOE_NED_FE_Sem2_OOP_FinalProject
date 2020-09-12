import tictactoe0 as tictactoe
from sys import exit

print("***********")
print("TIC-TAC-TOE")
print("***********")
print()

continue_playing = True
while continue_playing:
    game = tictactoe.Game()
    game.play()
    print()
    if play_again := input("Do you want to play again?[y/Y]: ").upper() != 'Y':
        continue_playing = False

print("Closing game...")
exit(0)

    





