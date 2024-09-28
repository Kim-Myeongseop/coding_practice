def solution(points, routes):
    answer = 0
    n = len(routes)
    row, col = 1, 1
    for r, c in points:
        if row < r:
            row = r
        if col < c:
            col = c
    
    # 보드에 각 위치에 dict를 만든다. 초 : 리스트
    board = [[{} for _ in range(col)] for _ in range(row)]
    
    # dict에 입력해 나가면서 초에 해당하는 count가 정확히 1일때 추가하는 경우만 count
    for route in routes:
        time = 0
        sr, sc = points[route[0]-1]   # 처음 시작점 미리 추가
        if board[sr-1][sc-1].get(time) == 1:
                    answer += 1
        board[sr-1][sc-1][time] = board[sr-1][sc-1].get(time, 0) + 1
        for i in range(1, len(route)):
            sr, sc = points[route[i-1]-1]   # start row, start col
            er, ec = points[route[i]-1]   # end row, end col
            sign_r = 1 if er >= sr else -1
            sign_c = 1 if ec >= sc else -1
            while sr != er:   # row 먼저
                sr += sign_r   # 이동 후 계산
                time += 1   # 이동 후 계산
                if board[sr-1][sc-1].get(time) == 1:
                    answer += 1
                board[sr-1][sc-1][time] = board[sr-1][sc-1].get(time, 0) + 1
            while sc != ec:
                sc += sign_c   # 이동 후 계산
                time += 1   # 이동 후 계산
                if board[sr-1][sc-1].get(time) == 1:
                    answer += 1
                board[sr-1][sc-1][time] = board[sr-1][sc-1].get(time, 0) + 1
    return answer
