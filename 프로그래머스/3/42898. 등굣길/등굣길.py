import math

def solution(m, n, puddles):   # n행 m열
    answer = 0
    board = [[0]*m for _ in range(n)]
    board[0][0] = 1
    for x, y in puddles:
        board[y-1][x-1] = None
        
    for r in range(n):
        for c in range(m):
            if board[r][c] != None:
                if r > 0:
                    a = board[r-1][c]
                    if a != None:
                        board[r][c] += a
                if c > 0:
                    b = board[r][c-1]
                    if b != None:
                        board[r][c] += b
            
    return board[n-1][m-1] % 1_000_000_007