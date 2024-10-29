from minimax import find_best_move
from connectfour import C4Board
from board import Move, Board


board = C4Board()


def get_player_move() -> Move:
    player_move: Move = Move(-1)
    while player_move not in board.legal_moves:
        play: int = int(input("Player move: "))
        player_move = Move(play)
    return player_move


if __name__ == "__main__":
    while True:
        human_move = get_player_move()
        board = board.move(human_move)
        if board.is_win:
            print("Human wins!")
            break
        elif board.is_draw:
            print("Draw!")
            break
        computer_move = find_best_move(board, 5)
        board = board.move(computer_move)
        print(board)
        if board.is_win:
            print("Computer wins!")
            break
        elif board.is_draw:
            print("Draw!")
            break
