from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0   # 거리
    
    # board 생성(0:inner, 1:boundary, -1:outer)
    board = [[-1 for _ in range(101)] for _ in range(101)]
    for x_min, y_min, x_max, y_max in rectangle:
        for r in range(2*(50-y_max), 2*(50-y_min)+1):
            for c in range(2*x_min, 2*x_max+1):
                if r == 2*(50-y_max) or r == 2*(50-y_min) or c == 2*x_min or c == 2*x_max:
                    if board[r][c] != 0:   # 이미 이전의 내부점으로 된 점은 제외
                        board[r][c] = 1
                else:
                    board[r][c] = 0
                    
    # search
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    q = deque()
    start = (characterX, characterY)
    q.append(start)
    visited = (-1, -1)   # 어차피 모든 길은 2개의 선택지 뿐이다. 즉, list로 관리할 필요가 없다.
    item_cnt = 1e+8
    while q:
        x, y = q.pop()
        if (x, y) == (itemX, itemY):
            item_cnt = answer
            answer = 0
        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]
            cx = nx + x   # (2*nx + 2*x)//2
            cy = (50-ny) + (50-y)   # (2*(50-ny) + 2*(50-y))//2
            if (0 <= nx <= 50) and (0 <= ny <= 50) and (board[2*(50-ny)][2*nx] == 1) and (board[cy][cx] == 1) and (nx,ny) not in [visited, start]:   # start와 직전 방문만 확인하면 된다.
                q.append((nx, ny))
                answer += 1
                break
        visited = (x, y)
        if item_cnt < answer:   # 출발 지점까지 이어서 진행하다가 처음 구한 거리가 최소임을 알 때 break
            break
    # 재도착지점 직전에 끝나기 때문에 재도착지점 직전에서 재도착지점까지 거리를 추가해준다.
    answer += 1
    return min(answer, item_cnt)