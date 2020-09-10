import copy

BOARD_DIMENSIONS = 3
X = 'X'
O = 'O'
EMPTY = None
X_utility, O_utility = -1, 1  # will be set by the method 'markers()' of class Game.


class Game:
    def __init__(self):
        self.board = Board()

    def play(self):
        human_marker, computer_marker = Game.markers()
        print(f"You'll play as {human_marker} and Computer will play as {computer_marker}.\n")
        print("Do you want to make the first move?")
        play_first = input("Yes[y/Y]: ").upper()
        if play_first == 'Y':
            self.player1 = Player(marker=human_marker)
            self.player2 = AI(marker=computer_marker)
        else:
            self.player1 = AI(marker=computer_marker)
            self.player2 = Player(marker=human_marker)
        print()

        self.gameloop()

        winner = self.board.winner()
        if winner is None:
            print("GAME TIED!")
        elif player1.marker == winner:
            if isinstance(player1, AI):
                print("COMPUTER WINS!")
            else:
                print("YOU WIN!")
        else:
            if isinstance(player1, AI):
                print("COMPUTER WINS!")
            else:
                print("YOU WIN!")

        print("GAME OVER.")

    @staticmethod
    def markers():
        '''
        Gets valid marker from user and returns that marker alongside
        the compliment of that marker
        '''
        global X_utility, O_utility
        print("Choose your marker:")
        while True:
            human_marker = input("'X' or 'O': ").upper()
            if human_marker == X:
                X_utility = -1
                O_utility = 1
                return human_marker, O
            elif human_marker == O:
                X_utility = 1
                O_utility = -1
                return human_marker, X
            print("Error, invalid marker.")
            print()

    def gameloop(self):
        current_player = 0  # 0 indicates player 1; 1 indicates player 2
        while not self.board.terminal():  # while the game isn't at a terminal state
            print(self.board)
            print()
            if current_player % 2 == 0:
                marker = self.player1.marker
                move = self.player1.make_move(self.board)
            else:
                marker = self.player2.marker
                move = self.player2.make_move(self.board)

            self.board.update(marker, move)
            current_player += 1


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
        self.free_positions = dict()
        for i in range(9):
            self.free_positions[i + 1] = next(empty_coordinates)

    def update(self, marker, coordinate):
        '''
        places the given marker at the cell at the given coordinate
        '''
        # print(self.free_positions)
        pos = Board.position_from_coordinate(coordinate)
        self.free_positions.pop(pos)
        x = coordinate[0]
        y = coordinate[1]
        self.grid[x][y].setMarker(marker)

    def terminal(self):
        """
        Returns True if game is over (someone has won or the grid is filled),
        False otherwise.
        """

        if self.winner() is not EMPTY:
            # print("x")
            return True

        # checking if any cell is empty
        for row in self.grid:
            for cell in row:
                if cell.marker is EMPTY:
                    return False

        return True

    def result(self, current_marker, move):
        """
        Returns the board that results from making move (i, j) on the board.
        """
        # check if the action is valid
        if (move[0] not in range(0, BOARD_DIMENSIONS)) or (move[1] not in range(0, BOARD_DIMENSIONS)):
            raise IndexError(f"Invalid action: {action}.")

        resultant_board = copy.deepcopy(self)
        resultant_board.update(current_marker, move)
        return resultant_board

    def utility(self):  ## bigTODO
        """
        Returns utility of the current board state: 0 if no one has won,
        else 1 or -1 depending on which player has won.
        """
        winning_marker = self.winner()
        if winning_marker is EMPTY:
            return 0
        elif winning_marker == X:
            return X_utility
        else:
            return O_utility

    def winner(self):
        '''
        if a winning pattern exists, returns the marker in that pattern,
        otherise returns None
        '''
        board = self.grid
        # Checking for vertical or horizontal winning pattern
        for i in range(BOARD_DIMENSIONS):
            if board[i][0].marker == board[i][1].marker == board[i][
                2].marker != EMPTY:  # if all markers in row i are same
                # print("here1")
                return board[i][0].marker
            elif board[0][i].marker == board[1][i].marker == board[2][
                i].marker != EMPTY:  # if all markers in column i are same
                # print("here2")
                return board[0][i].marker

        # Checking for diagonal winner
        if (board[0][0] == board[1][1] == board[2][2] != EMPTY) or (board[0][2] == board[1][1] == board[2][0] != EMPTY):
            # print("here3")
            return board[1][1].marker

        # print("here")

    def current_player_marker(self):
        """
        Returns the marker of the player who has the next turn
        on the current board state.
        """
        if self.terminal():
            return None

        # count number of X's and O's on board
        count_X, count_O = 0, 0
        for row in range(BOARD_DIMENSIONS):
            for col in range(BOARD_DIMENSIONS):
                if self.grid[row][col].marker == X:
                    count_X += 1
                elif self.grid[row][col].marker == O:
                    count_O += 1

        if count_X > count_O:
            return O
        else:
            return X

    @staticmethod
    def position_from_coordinate(coordinate):
        row, col = coordinate[0], coordinate[1]
        return (3 * row) + col + 1  # this formula gives for board positions from 1 to 9

    @staticmethod
    def coordinates_from_position(pos):
        if pos in range(1, 4):
            row = 0
        elif pos in range(4, 7):
            row = 0
        else:
            row = 2

        col = (pos - 1) - (3 * row)  # since position = (3 * row) + col + 1
        return (row, col)

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
                    board_str += f' ({Board.position_from_coordinate((row, col))}) ' + bar
                else:
                    board_str += f'  {marker}  ' + bar
            bar = "|"  # reset bar to original value for usage in next row
            if row != 2:  # no row divider needed after last row
                board_str += "\n"
                board_str += row_divider + "\n"

        return board_str


class Player:
    def __init__(self, marker):
        self.marker = marker

    def make_move(self, board):
        '''
        takes a board input, gets a valid position from the user
        to make on that board and returns the position.
        '''
        while True:
            print("-> Your move")
            try:
                print(board)
                pos = input("Enter the position where you want to make a move: ")
                pos = int(pos)
                if pos in board.free_positions:
                    return pos
                    # return Board.coordinates_from_position(pos)

                if pos in range(1, 10):
                    print(f"Position {pos} is already filled. Please choose another one.")
                else:
                    raise ValueError
            except ValueError:
                print(f"{pos} is not a valid board position. Please choose a valid position\
from the given board.\n")
            print()


class AI(Player):
    def make_move(self, board):
        '''takes a board state as input andreturns the optimal coordinate to make
        on the current board state; i.e the coordinate that will lead to a state
        with best utility possible from the current state.
        '''
        print("-> Computer's move")
        print(board)
        print("Computer thinking....")

        if board.terminal():
            return None
        free_coordinates = set(board.free_positions.values())
        best_utility_sofar = -1
        alpha, beta = -1, 1

        # find the maxiumum possible utility on the current board state if both players play optimally
        for coordinate in free_coordinates:
            # print("current action in consideration", coordinate)
            # print("min util if curr action taken:", AI.get_min_utility(board.result(self.marker, coordinate)))
            best_utility_sofar = max(best_utility_sofar,
                                     AI.get_min_utility(board.result(self.marker, coordinate), alpha, beta))
            if best_utility_sofar == 1:
                pos = Board.position_from_coordinates(coordinate)
                print(f"Position decided: {pos}")
                return pos
                # return Board.coordinates_from_position(pos)

        # find the coordinate that lead to the best possible utility calculated above
        for coordinate in free_coordinates:
            if AI.get_min_utility(board.result(self.marker, coordinate), alpha, beta) == best_utility_sofar:
                pos = Board.position_from_coordinate(coordinate)
                print(f"Position decided: {pos}")
                return pos

    @staticmethod
    def get_max_utility(state, alpha, beta):
        '''
        takes a board state as input and returns maximum possible utility for that state
        '''
        if state.terminal():
            return state.utility()
        free_coordinates = set(state.free_positions.values())
        max_utility = -1
        current_marker = X if X_utility == 1 else O

        for coordinate in free_coordinates:
            resultant_state = state.result(current_marker, coordinate)
            min_utility_resultant_state = AI.get_min_utility(resultant_state, alpha, beta)
            max_utility = max(max_utility, min_utility_resultant_state)
            alpha = max(alpha, min_utility_resultant_state)
            if beta <= alpha:
                return max_utility
        if max_utility == 1:  # we can stop and return 1 if utility of resultant state is 1 since thats the maximum possible utility
            return 1

        return max_utility

    @staticmethod
    def get_min_utility(state, alpha, beta):
        '''
        takes a board state as input and returns minimum possible utility for that state
        '''
        if state.terminal():
            return state.utility()
        free_coordinates = set(state.free_positions.values())
        min_utility = 1
        current_marker = X if X_utility == -1 else O
        for coordinate in free_coordinates:
            resultant_state = state.result(current_marker, coordinate)
            max_utility_resultant_state = AI.get_max_utility(resultant_state, alpha, beta)
            min_utility = min(min_utility, max_utility_resultant_state)
            beta = min(beta, max_utility_resultant_state)
            if beta <= alpha:
                return min_utility
        if min_utility == -1:  # we can stop and return -1 if utility of resultant state is -1 since thats the minimum possible utility
            return -1

        return min_utility


b = Board()
# b.update(X, (1, 1))
# b.update(O, (0, 0))
# b.update(X, (1, 0))

print(b)
print()
c = AI("O")
z = c.make_move(b)
print(z)
