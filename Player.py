#TODO: fix self.empty_positions and coordinates problem in class board init. Maybe store em together in dict? Then \
# work on  the makeMove method of Player()

X = "X"
O = "O"
EMPTY = None
BOARD_DIMENSIONS = 3

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
        self.empty_positions = set(range(1, 10))
        self.empty_coordinates = {(i, j) for i in range(BOARD_DIMENSIONS) for j in range(BOARD_DIMENSIONS)}
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
            bar = "|"  # reset bar to original value for usage in next row
            if row != 2:  # no row divider needed after last row
                board_str += "\n"
                board_str += row_divider + "\n"

        return board_str




class Player:
    def __init__(self, marker, utility):
        self.marker = marker
        self.utility = utility

    @staticmethod
    def coordinatesFromPosition(pos):
        if pos in range(1, 4):
            row = 0
        elif pos in range(4, 7):
            row = 0
        else:
            row = 2

        col = position - 1 - (3 * row)  # since position = (3 * row) + col + 1
        return (row, col)


    def makeMove(self, board):
        while True:
            try:
                print(board)
                pos = input("Enter the position where you want to make a move: ")
                pos = int(pos)
                if pos in board.empty_positions:
                    return coordinatesFromPosition(pos)
                if pos in range(1, 10):
                    print(f"Position {pos} is already filled. Please choose another one.")
                else:
                    raise ValueError
            except ValueError:
                print(f"{pos} is not a valid board position. Please choose a valid value from the given board.")
            print()
b = Board()
x = Player(X, 1)
print(x.makeMove(b))


