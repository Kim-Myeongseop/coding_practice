import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]   # 공백 없는 문자열은 split()이 안된다.
directions = [(1,0), (0,1), (-1,0), (0,-1)]

# 'R', 'B'의 위치 기억
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red_row, red_col = i, j
        if board[i][j] == 'B':
            blue_row, blue_col = i, j

def move(row, col, direction):
    dist = 0   # 이동 거리 측정 => 나중에 이 값을 이용하여, 'R', 'B' 중 먼저 도착한 공을 판단하기 위해
    y, x = row, col   # 현재 행, 열
    dy, dx = direction   # 이동 방향 (행, 열)
    # 현재가 'O' 이거나 이동 예정인 곳이 '#' 라면 stop
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        dist += 1
        y += dy
        x += dx
    return y, x, dist
            
search_list = deque()
search_list.append((red_row, red_col, blue_row, blue_col, 0))   # 공의 위치 상태 및 방문 횟수(cnt)
visited = []
visited.append((red_row, red_col, blue_row, blue_col))   # 횟수 상관없이 같은 상태가 되면 방문 처리
answer = -1
while search_list:
    ry, rx, by, bx, cnt = search_list.popleft()
    
    if cnt >= 10:
        break
        
    for i in range(4):   # 현재 위치(ry, rx, by, bx) 기준으로 4방향 탐색
        nry, nrx, rdist = move(ry, rx, directions[i])
        nby, nbx, bdist = move(by, bx, directions[i])
        
        if board[nby][nbx] == 'O':   # 파란 공이 빠졌으면 다음 방향 조회(동시에 빠져도 종료)
            continue
        if board[nry][nrx] == 'O':   # 파란 공이 빠지지 않고, 빨간 공이 빠졌으면 종료
            answer = cnt + 1   # 함수 방식이 아니므로 answer를 쓸 수 없다. 두 번 break 해주자
            break
            
        if nry==nby and nrx==nbx:   # 위치가 같으면 누가 먼저 도착했는지 판단 후 한 칸 뒤로
            if rdist > bdist:   # 'B'가 먼저 도착
                nry -= directions[i][0]
                nrx -= directions[i][1]
            else:   # 'R'이 먼저 도착
                nby -= directions[i][0]
                nbx -= directions[i][1]
            
        if (nry, nrx, nby, nbx) not in visited:
            visited.append((nry, nrx, nby, nbx))
            search_list.append((nry, nrx, nby, nbx, cnt+1))
    
    if answer > -1:   # answer가 -1이 아니게 되면 return(위에서 첫번째 break를 만나면 여기로 옴)
        break

print(answer)
        
    