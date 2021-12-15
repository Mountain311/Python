# import chess library for using chess moves,board etc 
import chess
import time

# alpha beta function  
 
def alphabeta(board, depth, alpha, beta, maximize): 
    if board.is_checkmate(): 
        return -40 if maximize else 40 
    elif board.is_game_over(): 
        return 0 
 
    if depth == 0: 
        return boardValue(board) 
 
    if maximize: 
        bestValue = float("-inf") 
        for move in board.legal_moves: 
            experimentBoard = board.copy() 
            experimentBoard.push(move) 
            value = alphabeta(experimentBoard, depth, alpha, beta, False) 
            bestValue = max(bestValue, value) 
            alpha = max(alpha, bestValue) 
            if alpha >= beta: 
                break 
        return bestValue 
    else: 
        bestValue = float("inf") 
        for move in board.legal_moves: 
            experimentBoard = board.copy() 
            experimentBoard.push(move) 
            value = alphabeta(experimentBoard, depth - 1, alpha, beta, True) 
            bestValue = min(bestValue, value) 
            beta = min(beta, bestValue) 
            if alpha >= beta: 
                break 
        return bestValue 
 
    return 0 