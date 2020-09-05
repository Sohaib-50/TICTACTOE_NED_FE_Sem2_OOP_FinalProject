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

        while not self.board.terminal():
            print(board)
            print()
            if current_player % 2 == 0:
                marker = player1.marker
                move = player1.make_move(self.board)
            else:
                marker = player2.marker
                move = player2.make_move(self.board)

            self.board.update(marker, move)
            current_player += 1

    def play(self):
        human_marker, computer_marker = get_markers()
        print(f"You'll play as {human_marker} and Computer will play as {computer_marker}.\n")
        print("Do you want to make the first move?")
        play_first = input("Yes[y/Y]: ").upper()
        if play_first == 'Y':
            self.player1 = ttt.Player(marker=human_marker, utility=-1)
            self.player2 = ttt.AI(marker=computer_marker, utility=1)
        else:
            self.player1 = ttt.AI(marker=computer_marker, utility=1)
            self.player2 = ttt.Player(marker=human_marker, utility=-1)
        print()

        self.gameloop()

        winner = self.board.winner()
        if winner None:
            print("GAME TIED!")
        else if player1.marker == winner:
            if isinstance(player1, AI)

        @staticmethod
        def get_markers():
            '''
            Gets valid marker from user and returns that marker alongside
            the compliment of that marker
            '''
            print("Choose your marker:")
            while True:
                human_marker = input("'X' or 'O': ").upper()
                if human_marker == X:
                    return human_marker, O
                elif human_marker == O:
                    return human_marker, X
                print("Error, invalid marker.")
                print()


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
        self.grid = [[Cell(coordinates=(row, col)) for col in range(BOARD_DIMENSIONS)] for row in
                     range(BOARD_DIMENSIONS)]
        empty_coordinates = ((i, j) for i in range(BOARD_DIMENSIONS) for j in range(BOARD_DIMENSIONS))
        self.empty_positions = dict()
        for i in range(9):
            self.empty_positions[i + 1] = next(empty_coordinates)

    def update(self, marker, position):
        '''
        places the given marker at the given position's cell
        '''
        coordinates = self.empty_positions.pop(position)
        x = coordinates[0]
        y = coordinates[1]
        self.grid[x][y].setMarker(marker)

    def terminal(self):
        """
        Returns True if game is over (someone has won or the grid is filled),
        False otherwise.
        """

        if self.winner() is not None:
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


    def utility(grid):  ## bigTODO
        """
        Returns utility of the current board state: 0 if no one has won,
        else 1 or -1 depending on which player has won.
        """
        winning_marker = winner(grid)
        if winning_marker is EMPTY:
            return 0
        elif winning_marker == player1.marker:
            return player1.utility
        else:
            return player2.utility

    def winner(self):
        '''
        if a winning pattern exists, returns the marker in that pattern,
        otherise returns None
        '''
        board = self.grid
        # Checking for vertical or horizontal winning pattern
        for i in range(BOARD_DIMENSIONS):
            if board[i][0].marker == board[i][1].marker == board[i][2].marker != EMPTY:  # if all markers in row i are same
                return board[i][0].marker
            elif board[0][i].marker == board[1][i].marker == board[2][i].marker != EMPTY:  # if all markers in column i are same
                return board[0][i].marker

        # Checking for diagonal winner
        if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
            return board[1][1].marker


    def __str__(self):
        '''returns the board in a pretty printable format'''
        board_str = ""  # the string that will be returned
        five_dashes = '-' * 5
        bar = "|"
        row_divider = five_dashes + "+" + five_dashes + "+" + five_dashes

        for row in range(BOARD_DIMENSIONS):
            for col in range(BOARD_DIMENSIONS):
                marker = self.grid[row][col].marker
                if col == 2:  # no need to add a bar if last element of row
                    bar = ''
                if marker is EMPTY:
                    board_str += f' ({(3 * row) + col + 1}) ' + bar  # ((3 * row) + col + 1) formula gives numbers for board positions from 1 to 9
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

    def make_move(self, board):
        '''
        takes a board input, gets a valid position from the user
        to make on that board and returns the position.
        '''
        while True:
            try:
                print(board)
                pos = input("Enter the position where you want to make a move: ")
                pos = int(pos)
                if pos in board.empty_positions:
                    return pos
                if pos in range(1, 10):
                    print(f"Position {pos} is already filled. Please choose another one.")
                else:
                    raise ValueError
            except ValueError:
                print(f"{pos} is not a valid board position. Please choose a valid position\
from the given board.\n")
            print()







