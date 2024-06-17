def solution(board):
    answer = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    board = [[c if c != 'R' else 0 for c in row] for row in board]
    idx = 0
    while idx < 10000:
        cnt = 0   # 새로운 idx에 해당하는 값이 하나도 없을 때, 더 이상 업데이트 불가하므로 return -1
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == idx:
                    cnt += 1
                    # search start
                    for k in range(4):
                        x, y = j, i
                        while True:
                            if (0 <= y+dy[k] < len(board)) and (0 <= x+dx[k] < len(board[i])):
                                y += dy[k]
                                x += dx[k]
                            else:
                                break
                            if board[y][x] == 'D':
                                y -= dy[k]
                                x -= dx[k]
                                break
                        if board[y][x] == '.':
                            board[y][x] = idx+1
                        if board[y][x] == 'G':
                            return idx+1
        idx += 1
        if cnt == 0:
            return -1
    return answer