import numpy as np
from multiprocessing import Pool
from scipy import signal

def prRed(skk): return f"\033[91m {skk}\033[00m"
def prPurple(skk): return f"\033[95m {skk}\033[00m"
def prLightGray(skk): return f"\033[97m {skk}\033[00m"

boardsize = (6, 8)
icons = {1: prRed('O'), 0: prLightGray('.'), -1: prPurple('O')}

def display(board, isRed):
    print(' ' + '  '.join([str(i) for i in range(len(board[0]))]))
    sign = 1 if isRed else -1
    print('\n'.join([' '.join([icons[item*sign] for item in row])
        for row in board]))
    
inf = 10**10

DEPTH = 6

PROCESS_CT = 12

WIN_CONDS = [
    np.array([[1], [1], [1], [1]]),
    np.array([[1, 1, 1, 1]]),
    
    np.array(
        [[1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]]),
         
    np.array(
        [[0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0]])
]

def alphaBeta(node, depth, alpha, beta, history=None, max_depth=DEPTH):
    if depth == max_depth:
        history = {move: 0 for move in validMoves(node.board)}
        
    if depth == 0 or node.isTerminal():
        return scoreBoard(node.board, depth)
    
    if node.isMaximizingPlayer():
        value = -inf 
        for child, move in node.getChildren(history):
            value = max(value, alphaBeta(child, depth-1, alpha, beta, history))
            
            alpha = max(alpha, value)
            if alpha >= beta:
                history[move] += 2**depth
                break
        return value
    else:
        value = inf
        for child, move in node.getChildren(history):
            value = min(value, alphaBeta(child, depth-1, alpha, beta, history))
            beta = min(beta, value)
            if alpha >= beta:
                history[move] += 2**depth
                break
        return value
    
class PlayerNode:
    def __init__(self, board):
        self.board = board
        self.player = 1
        
    def getChildren (self, history):
        children = []
        moves = validMoves(self.board)
        moves = sorted(moves, key=lambda x: -history[x])
        children = []
        for move in moves:
            new_board = placePiece(self.board, move, player = self.player)
            children.append((EnemyNode(new_board), move))
        return children
    
    def isTerminal(self):
        return isWin(self.board) or isDraw(self.board)
    
    def isMaximizingPlayer(self):
        return True
    
    
class EnemyNode:
    def __init__(self, board):
        self.board = board
        self.player = -1
        
    def getChildren (self, history):
        children = []
        moves = validMoves(self.board)
        moves = sorted(moves, key=lambda x: -history[x])
        for move in moves:
            new_board = placePiece(self.board, move, player=self.player)
            children.append((PlayerNode(new_board), move))
        return children
    
    def isTerminal(self):
        return isLoss(self.board) or isDraw(self.board)
    
    def isMaximizingPlayer(self):
        return False
    
def scorePlayerBoard(board):
    convs = [signal.convolve2d(board, cond, mode='valid')
             for cond in WIN_CONDS]
    flat_convs = np.array([i for conv in convs for row in conv for i in row])
    best = np.max(flat_convs)
    threes = np.sum(flat_convs == 3)
    twos = np.sum(flat_convs == 2)
    score = best + threes/10 + twos/100
    score = min(4, score)
    return score

def scoreBoard(board, depth):
    player_score = scorePlayerBoard(board)
    score = player_score - depth/1000
    if isWin(board):
        score = 4
    if isLoss(board):
        score = -4
    return score

def isLoss(board):
    return isWin(board*-1)

def isWin(board):
    convs = [signal.convolve2d(board, cond) for cond in WIN_CONDS]
    result = any ([i == 4
                   for conv in convs
                   for row in conv
                   for i in row])
    return result

def isDraw(board):
    no_win = not isWin(board) and not isLoss(board)
    no_moves = board.size == 0
    return no_win and no_moves

def validMoves(board):
    result = [idx for idx, value in enumerate(board[0]) if value == 0]
    return np.array(result)

def placePiece(board, colnum, player=1):
    lastEmptyRow = np.where(board[:, colnum] == 0) [0][-1]
    new_board = np.copy(board)
    new_board[lastEmptyRow, colnum] = player
    return new_board

def processNode(node):
    score = alphaBeta(node, DEPTH, -inf , inf)
    return score

def playMove(board):
    moves = validMoves(board)
    
    next_boards = [placePiece(board, move, player=1) for move in moves]
    next_nodes = [EnemyNode(board) for board in next_boards]
    with Pool(PROCESS_CT) as p:
        scores = p.map(processNode, next_nodes)
    moves_scores = sorted(zip(moves, scores), key=lambda x: x[1])
    best_move = moves_scores[-1][0]
    return best_move

if __name__ == '__main__':
    board = np.zeros(boardsize)
    isRed = False
    while not isWin(board) and not isLoss(board) and not isDraw(board):
        isRed = not isRed
        display(board, isRed)
        print ('='*30)
        
        board = board*-1
        comp_move = playMove(board)
        board = placePiece(board, comp_move, player=1)
        if isWin(board) or isLoss(board) or isDraw(board):
            break
        
    print ('GAME OVER')
    display(board, not isRed)