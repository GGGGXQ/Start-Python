from board import Piece, Board, Move


def minimax(board: Board, maximizing: bool, original_player: Piece, max_depth: int = 8) -> float:
    if board.is_win or board.is_draw or max_depth == 0:
        return board.evaluate(original_player)

    if maximizing:
        best_eval: float = float("-inf")
        for move in board.legal_moves:
            result: float = alphabeta(board.move(move), False, original_player, max_depth - 1)
            best_eval = max(result, best_eval)
        return best_eval
    else:
        worst_eval: float = float("inf")
        for move in board.legal_moves:
            result = alphabeta(board.move(move), True, original_player, max_depth - 1)
            worst_eval = min(worst_eval, result)
        return worst_eval


def find_best_move(board: Board, max_depth: int = 8) -> Move:
    best_eval = float("-inf")
    best_move = Move(-1)
    for move in board.legal_moves:
        result: float = minimax(board.move(move), False, board.turn, max_depth)
        if result > best_eval:
            best_move = move
            best_eval = result
    return best_move


def alphabeta(board: Board, maximizing: bool, original_player: Piece, max_depth: int = 8,
              alpha: float = float("-inf"), beta: float = float("inf")) -> float:
    if board.is_win or board.is_draw or max_depth == 0:
        return board.evaluate(original_player)

    if maximizing:
        for move in board.legal_moves:
            result: float = alphabeta(board.move(move), False, original_player, max_depth - 1, alpha, beta)
            alpha = max(alpha, result)
            if alpha >= beta:
                break
        return alpha
    else:
        for move in board.legal_moves:
            result = alphabeta(board.move(move), True, original_player, max_depth - 1, alpha, beta)
            beta = min(beta, result)
            if beta <= alpha:
                break
        return beta
