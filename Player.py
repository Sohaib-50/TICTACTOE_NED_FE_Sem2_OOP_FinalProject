# TODO: Then \
# work on  the makeMove method of Player()

X = "X"
O = "O"
EMPTY = None
BOARD_DIMENSIONS = 3










board = Board()
current_player = 0  # 0 indicates player 1; 1 indicates player 2
player1 = Player("X", 1)
player2 = Player("O", -1)
while True:
    print("\n" * 2)
    if current_player % 2 == 0:
        print(">>Your Turn\n")
        marker = player1.marker
        move = player1.make_move(board)
    else:
        print(">>Computer's Turn")
        marker = player2.marker
        move = player2.make_move(board)

    board.update(marker, move)


    current_player += 1
