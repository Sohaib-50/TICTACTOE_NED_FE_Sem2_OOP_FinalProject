#!/usr/bin/python
#-*- coding: utf-8 -*-
from Cell import Cell
import copy

class Board:
    def __init__(self):
        self.empty_positions = {(i, j) for i in range(3) for j in range(3)}
        self.grid = [Cell((i, j) for i in range(3) for j in range(3))]

    def update(self, marker. coordinates):
        '''
        places the given marker at the cell with given coordinates
        '''
        x = coordinates[0]
        y = coordinates[1]
        self.grid[x][y].setMarker(marker)

    def terminal(self):
        def terminal(board):
        """
        Returns True if game is over (someone has won or the grid is filled),
        False otherwise.
        """
        if winner(board) is not None:
            return True
        
        # checking if any cell is empty
        for row in self.grid:
            if EMPTY in row:
                return False
                    
        return True

    def result(self, action):
        """
        Returns the board that results from making move (i, j) on the board.
        """
        # check if the action is valid
        if action[0] not in range(0, BOARD_DIMENSIONS) or action[1] not in range(0, BOARD_DIMENSIONS):
            raise IndexError(f"Invalid action: {action}.")
        
    resultant_board = copy.deepcopy(board)
    current_player = player(board)
    resultant_board[action[0]][action[1]] = current_player.marker


    def actions(self):
        pass

    def utility(grid):  ## bigTODO
        """
        Returns 1 if  the game state is such that
        X has won the game, -1 if O has won, 0 otherwise.
        """
        winner_returnVal = winner(grid)
        if winner_returnVal == X:
            return 1
        elif winner_returnVal == O:
            return -1
        else:
            return 0

    def nextPlayer(self):
        """
        Returns player who has the next turn on a board.
        """
        if terminal(board):
            return None
            
        # count number of X's and O's on board
        count_X, count_O = 0, 0
        for i in range(BOARD_DIMENSIONS):
            for j in range(BOARD_DIMENSIONS):
                    if board[i][j] == X:
                            count_X += 1
                    elif board[i][j] == O:
                            count_O += 1
                            
        if count_X > count_O:
            return O
        else:
            return X

    def winner(self, ):
        pass

    def __repr__(self):
        pass

