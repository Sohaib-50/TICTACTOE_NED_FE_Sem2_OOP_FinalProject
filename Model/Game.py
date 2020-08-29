#!/usr/bin/python
#-*- coding: utf-8 -*-

class Game:
    def __init__(self):
        print("Choose your marker:")
        human_marker = input("'X' or 'O': ").upper()
        if human_marker == X:
            computer_marker = O
        elif human_marker = O:
            computer_marker = X
        else:
            raise Exception('Invalid marker entered')
        print(f"You'll play as {marker} and Computer will play as {computer_marker}")
        print()

        print("Do you want to make the first move?")
        play_first = input("Yes [y/Y] or No[N/n]: ").lower()
        if play_first == 'y':
            self.player1 = Player(marker=human_marker, utility=1)
            self.player2 = AI(marker=computer_marker, utility=-1)
        elif play_first == 'n':
            self.player1 = AI(marker=computer_marker, utility=1)
            self.player2 = Player(marker=human_marker, utility=-1)
        else:
            Exception("Invalid input (not y/n)")
        print()

        self.board = Board()
        
        

    def play(self):
        current_player = 0  # 0 indicates player 1, 1 indicates player 2

        while not self.over():
            print(board)
            print()
            if current_player = 0:
                marker = player1.marker
                move = player1.makeMove()
            else:
                marker = player2.marker
                move = player2.makeMove()

            self.board.update(marker, move)

            if self.board.terminal():
                

    def Operation1(self, ):
        pass

