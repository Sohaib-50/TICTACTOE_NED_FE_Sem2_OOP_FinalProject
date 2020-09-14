import tictactoe1 as tictactoe
from sys import exit

print("***********")
print("TIC-TAC-TOE")
print("***********")
print()

def get_game_mode() -> str:
    print("Choose game mode:")
    while True:
        mode = input("Press s/S for single player mode (play vs computer); t/T for two player mode: ").upper()
        if mode == 'S' or mode == 'T':
            return mode
        else:
            print("Invalid mode. Please re-enter.\n")

while 1 < 2:
    if get_game_mode() == 'S':
        game = tictactoe.SinglePlayerMode()
    else:
        game = tictactoe.TwoPlayerMode()
    print()
    game.play()
    print()
    if input("Enter y/Y if you want to play again: ").upper() != 'Y':
        break
    print("Okay restarting game.")
    print("\n" * 4)

print("Closing game.")
exit(0)







