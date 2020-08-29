import copy

BOARD_DIMENSIONS = 3
X = 'X'
O = 'O'
EMPTY = None


class Game:
    def __init__(self):
        self.board = Board()

    def gameloop(self):
        current_player = 0  # 0 indicates player 1; 1 indicates player 2

        while not self.over():
            print(board)
            print()
            if current_player == 0:
                marker = player1.marker
                move = player1.makeMove(self.board)
            else:
                marker = player2.marker
                move = player2.makeMove(self.board)

            self.board.update(marker, move)

            if self.board.terminal():
                break

    def play(self):
        print("Choose your marker:")
        human_marker = input("'X' or 'O': ").upper()
        if human_marker == X:
            computer_marker = O
        elif human_marker == O:
            computer_marker = X
        else:
            raise Exception('Invalid marker entered')
        print(f"You'll play as {human_marker} and Computer will play as {computer_marker}")
        print()

        print("Do you want to make the first move?")
        play_first = input("Yes[y/Y] or No[N/n]: ").upper()
        if play_first == 'Y':
            self.player1 = ttt.Player(marker=human_marker, utility=-1)
            self.player2 = ttt.AI(marker=computer_marker, utility=1)
        elif play_first == 'N':
            self.player1 = ttt.AI(marker=computer_marker, utility=1)
            self.player2 = ttt.Player(marker=human_marker, utility=-1)
        else:
            Exception("Invalid input for play_first (not y/n)")
        print()

        self.gameloop()

        winner = self.board.winner()
        if winner None:
            print("GAME TIED!")
        else if player1.marker == winner:
            if isinstance(player1, ttt.AI)




class Cell:
    def __init__(self, coordinates):
        self.marker = EMPTY
        self.__coordinates = coordinates

    def getCoordinates(self):
        return self.__coordinates

    def setMarker(self, marker):  # TODO: make marker a PROPERTY
        self.marker = marker

    def __repr__(self):
        return f"<Cell; Coordinates={self.__coordinates}, Marker={self.marker}>"



class Board:
    def __init__(self):
        self.empty_positions = {(i, j) for i in range(BOARD_DIMENSIONS) for j in range(BOARD_DIMENSIONS)}
        self.grid = [[Cell((row, col)) for col in range(BOARD_DIMENSIONS)] for row in range(BOARD_DIMENSIONS)]

    def update(self, marker, coordinates):
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
            pass

    def winner(self, ):
        pass

    def __str__(self):
        board_str = ""  # the string that will be returned
        dashes = '-' * 5
        bar = "|"
        row_divider = dashes + "+" + dashes + "+" + dashes
        for row in range(BOARD_DIMENSIONS):
            for col in range(BOARD_DIMENSIONS):
                marker = self.grid[row][col].marker
                if col == 2:  # no need to add a bar if last element of row
                    bar = ''
                if marker is EMPTY:
                    board_str += f' ({(3 * row) + col + 1}) ' + bar   # ((3 * row) + col + 1) formula gives numbers for board positions from 1 to 9
                else:
                    board_str += f'  {marker}  ' + bar
            board_str += "\n"
            bar = "|"  # reset bar to original value for usage in next row
            if row != 2:  # no row divider needed after last row
                board_str += row_divider + "\n"

        return board_str






