from minimax import find_best_move
from tictactoe import TTTBoard
from board import Board, Move


board: Board = TTTBoard()


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
        computer_move: Move = find_best_move(board)
        print(f"Computer move: {computer_move}")
        board = board.move(computer_move)
        if board.is_win:
            print("Computer wins!")
            break
        elif board.is_draw:
            print("Draw!")
            break
    print(board)
