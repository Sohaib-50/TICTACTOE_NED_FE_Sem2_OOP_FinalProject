## TODO : use coordinates of cell() to highlight and display winning combination at end

from __future__ import annotations
from typing import Optional
from abc import ABC, abstractmethod
from copy import deepcopy

# Constants
BOARD_DIMENSIONS = 3
X = 'X'
O = 'O'
EMPTY = None



class Game(ABC):
    X_utility, O_utility = 0, 0

    def __init__(self):
        self.board = Board()

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def markers_setup(x):
        pass

    def gameloop(self):
        current_player = 0  # 0 indicates player 1; 1 indicates player 2
        while not self.board.terminal():  # while the game isn't at a terminal state
            print("\n" * 2)
            if current_player % 2 == 0:
                marker = self.player1.marker
                coordinate = self.player1.make_move(self.board)
            else:
                marker = self.player2.marker
                coordinate = self.player2.make_move(self.board)
            self.board.update(marker, coordinate)
            current_player += 1


    def display_winner(self):
        winner = self.board.winner()
        if winner is None:
            print("<<<IT'S A TIE!>>>")
        elif self.player1.marker == winner:
            print(f"<<<{self.player1.alias} ({self.player1.marker}) WINS!>>>")
        else:
            print(f"<<<{self.player2.alias} ({self.player2.marker}) WINS!>>>")


class singlePlayerMode(Game):
    def play(self):
        human_marker, computer_marker = self.markers_setup()
        print(f"You'll play as {human_marker} and Computer will play as {computer_marker}.\n")
        print("Do you want to make the first move?")
        play_first = input("Enter y/Y if yes: ").upper()
        if play_first == 'Y':
            self.player1 = Player(marker=human_marker, alias="Your")
            self.player2 = AI(marker=computer_marker, alias="Computer")
        else:
            self.player1 = AI(marker=computer_marker, alias="Computer")
            self.player2 = Player(marker=human_marker, alias="Your")
        print()

        self.gameloop()
        print("\n" * 2)

        print("-> GAME OVER")
        print(self.board, "\n")
        self.display_winner()


    def markers_setup(self):
        '''
        Gets valid marker from user and returns that marker alongside
        the compliment of that marker (as computer's marker)
        '''
        print("Choose your marker:")
        while True:
            human_marker = input("'X' or 'O': ").upper()
            if human_marker == X:
                Game.X_utility = -1
                Game.O_utility = 1
                return human_marker, O
            elif human_marker == O:
                Game.X_utility = 1
                Game.O_utility = -1
                return human_marker, X
            else:
                print("Error, invalid marker.")



class twoPlayerMode(Game):
    def play(self):
        p1_marker, p2_marker = self.markers_setup()
        print(f"Player 1 will play as {p1_marker} and Player 2 as {p2_marker}.\n")
        self.player1 = Player(marker=p1_marker, alias="Player 1")
        self.player2 = Player(marker=p2_marker, alias="Player 2")

        self.gameloop()

        print("\n" * 2)
        print("-> GAME OVER")
        print(self.board, "\n")
        self.display_winner()


    def markers_setup(self):
        '''
        Gets valid marker from player 1 and returns that marker alongside
        the compliment of that marker (as player 2's marker)
        '''
        print("Player 1 choose your maker:")
        while True:
            p1_marker = input("'X' or 'O': ").upper()
            if p1_marker == X:
                return p1_marker, O
            elif p1_marker == O:
                return p1_marker, X
            else:
                print("Error, invalid marker.")



class Cell:
    def __init__(self, coordinate):
        self.marker = EMPTY
        self.__coordinate = coordinate


    def getCoordinates(self):
        return self.__coordinate


    def setMarker(self, marker):  # TODO: make marker a PROPERTY?
        self.marker = marker


    def __repr__(self):
        return f"< {self.marker}, {self.__coordinate} >"


    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.marker == other.marker
        else:
            return self.marker == other



class Board:
    def __init__(self):
        self.grid = [ [Cell(coordinate=(row, col)) for col in range(BOARD_DIMENSIONS)] for row in range(BOARD_DIMENSIONS) ]
        self.empty_coordinates = {(i, j) for i in range(BOARD_DIMENSIONS) for j in range(BOARD_DIMENSIONS)}


    def update(self, marker: str, coordinate: tuple) -> None:
        '''
        places the given marker at the cell at the given coordinate
        '''
        self.empty_coordinates.remove(coordinate)
        x = coordinate[0]
        y = coordinate[1]
        self.grid[x][y].setMarker(marker)


    def terminal(self) -> bool:
        """
        Returns True if game is over (someone has won or the grid is filled),
        False otherwise.
        """
        if self.winner() is not None:
            return True

        # checking if any cell is empty
        for row in self.grid:
            for cell in row:
                if cell.marker is EMPTY:
                    return False

        return True


    def winner(self) -> Optional[str]:
        '''
        if a winning pattern exists, returns the marker in that pattern,
        otherise returns None
        '''
        board = self.grid

        # Checking for vertical or horizontal winning pattern
        for i in range(BOARD_DIMENSIONS):
            # if all markers in row i are same and not empty
            if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0].marker is not EMPTY):
                return board[i][0].marker
            # if all markers in column i are same

            elif (board[0][i] == board[1][i] == board[2][i]) and (board[0][i].marker is not EMPTY):
                return board[0][i].marker

        # Checking for diagonal winner
        if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
            if board[1][1].marker is not EMPTY:
                return board[1][1].marker


    def result(self, current_marker: str, coordinate: tuple) -> Board:
        """
        Returns the board that results from placing current_marker at given coordinate on the board.
        """
        # check if the coordinate is valid
        if (coordinate[0] not in range(0, BOARD_DIMENSIONS)) or (coordinate[1] not in range(0, BOARD_DIMENSIONS)):
            raise IndexError(f"Invalid coordinate: {coordinate}.")

        resultant_board = deepcopy(self)
        resultant_board.update(current_marker, coordinate)
        return resultant_board


    def set_utilities(self, x: int, o: int):
        Game.X_utility = x
        Game.O_utility = o


    def utility(self) -> int:
        """
        Returns utility of the current board state: 0 if no one has won,
        else 1 or -1 depending on which player has won.
        """
        winning_marker = self.winner()
        if winning_marker is EMPTY:
            return 0
        elif winning_marker == X:
            return Game.X_utility
        else:
            return Game.O_utility


    @staticmethod
    def position_from_coordinate(coordinate: tuple) -> int:
        row, col = coordinate[0], coordinate[1]
        return (3 * row) + col + 1  # this formula gives for board positions from 1 to 9

    @staticmethod
    def coordinate_from_position(pos: int) -> tuple:
        if pos in range(1, 4):
            row = 0
        elif pos in range(4, 7):
            row = 1
        else:
            row = 2

        col = pos - 1 - (3 * row)  # since position = (3 * row) + col + 1
        return (row, col)


    def __str__(self) -> str:
        '''
        returns the board in a pretty printable format
        '''
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
                    board_str += f'  {Board.position_from_coordinate((row, col))}  ' + bar
                else:
                    board_str += f'  {marker}  ' + bar
            bar = "|"  # reset bar to original value for usage in next row
            if row != 2:  # no row divider needed after last row
                board_str += "\n"
                board_str += row_divider + "\n"

        return board_str



class Player:
    def __init__(self, marker: str, alias: str) -> None:
        self.marker = marker
        self.alias = alias
        x = marker


    def make_move(self, board: Board) -> tuple:
        '''
        takes a board input, gets a valid position from the user
        to make on that board and returns the position.
        '''
        print(f"-> {self.alias} ({self.marker}) turn")
        print(board)
        while True:
            try:
                pos = input("Enter the position where you want to make you move: ")
                pos = int(pos)
                coordinate = board.coordinate_from_position(pos)
                if coordinate in board.empty_coordinates:
                    return coordinate
                if pos in range(1, 10):
                    print(f"Position {pos} is already filled. Please choose another one.")
                else:
                    raise ValueError
            except ValueError:
                print(f"{pos} is not a valid board position. Please choose a valid position \
from the given board.")
            print()




class AI(Player):
    def __init__(self, marker, alias="Computer"):
        super().__init__(marker, alias)

    def make_move(self, board):
        '''takes a board state as input and returns the optimal coordinate to make
        on the current board state; i.e the coordinate that will lead to a state
        with best utility possible from the current state.
        '''
        print(f"-> {self.alias} ({self.marker}) turn")
        print(board)
        print("Computer thinking....")

        if board.terminal():
            return None

        best_utility_sofar = -1
        alpha, beta = -1, 1
        empty_coordinates = board.empty_coordinates

        # find the maxiumum possible utility on the input board state if both players play optimally
        for coordinate in empty_coordinates:
            best_utility_sofar = max(best_utility_sofar, AI.get_min_utility(board.result(self.marker, coordinate), alpha, beta))
            if best_utility_sofar == 1:
                pos = Board.position_from_coordinate(coordinate)
                print(f"Position decided: {pos}")
                return coordinate

        # find the coordinate that lead to the best possible utility calculated above
        for coordinate in empty_coordinates:
            if AI.get_min_utility(board.result(self.marker, coordinate), alpha, beta) == best_utility_sofar:
                pos = Board.position_from_coordinate(coordinate)
                print(f"Position decided: {pos}")
                return coordinate


    @staticmethod
    def get_max_utility(state, alpha, beta):
        '''
        takes a board state as input and returns maximum possible utility for that state
        '''
        if state.terminal():
            return state.utility()
        max_utility = -1
        current_marker = X if Game.X_utility == 1 else O # assign the max utility marker

        for coordinate in state.empty_coordinates:
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
        min_utility = 1
        current_marker = X if Game.X_utility == -1 else O  # assign the min utility marker
        for coordinate in state.empty_coordinates:
            resultant_state = state.result(current_marker, coordinate)
            max_utility_resultant_state = AI.get_max_utility(resultant_state, alpha, beta)
            min_utility = min(min_utility, max_utility_resultant_state)
            beta = min(beta, max_utility_resultant_state)
            if beta <= alpha:
                return min_utility
            if min_utility == -1:  # we can stop and return -1 if utility of resultant state is -1 since thats the minimum possible utility
                return -1

        return min_utility
