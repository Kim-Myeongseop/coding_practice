from collections import deque

# box 좌표를 받아서 좌측하단 점을 원점으로 평행이동시킨 matrix를 만들어준다.
def make_matrix(box_list):
    y_list = []
    x_list = []
    for y, x in box_list:
        y_list.append(y)
        x_list.append(x)
    min_y, min_x = min(y_list), min(x_list)
    max_y, max_x = max(y_list), max(x_list)
    
    matrix = [[0]*(max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for y, x in box_list:
        matrix[y - min_y][x - min_x] = 1
    return matrix

# matrix를 받아서 시계 방향으로 90도 회전한 matrix를 return하는 함수
def rotate_matrix(matrix):
    m, n = len(matrix), len(matrix[0])   # m행 n열
    rotated = [[0]*m for _ in range(n)]   # n행 m열
    for i in range(n):
        for j in range(m):
            rotated[i][j] = matrix[j][n-1-i]
    return rotated

def check(empty, block):
    empty = make_matrix(empty)
    block = make_matrix(block)
    for i in range(4):
        if i == 0:
            if empty == block:
                return True
        else:
            empty = rotate_matrix(empty)
            if empty == block:
                return True
    return False

def solution(game_board, table):
    answer = 0
    n = len(game_board)
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    
    # 블록을 모은다. : 알아 보기 좋게 함수화하지 않음.
    visited = [[False]*n for _ in range(n)]
    block_list = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not visited[i][j]:   # 블록에 해당하고, 방문 안했다면
                q = deque()
                q.append((i,j))
                block = []   # block을 구성하는 좌표를 모은다.
                while q:
                    y, x = q.popleft()   # 방문
                    visited[y][x] = True   # 방문 처리
                    block.append((y,x))
                    for dy, dx in directions:
                        if (0 <= y + dy < n) and (0 <= x + dx < n):
                            if table[y+dy][x+dx] == 1 and not visited[y+dy][x+dx]:
                                q.append((y+dy, x+dx))
                block_list.append(set(block))                
    
    # 빈공간 뭉치를 모은다. : 알아 보기 좋게 함수화하지 않음.
    visited = [[False]*n for _ in range(n)]
    empty_list = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and not visited[i][j]:   # 빈공간에 해당하고, 방문 안했다면
                q = deque()
                q.append((i,j))
                empty = []   # 빈공간 뭉치(empty)을 구성하는 좌표를 모은다.
                while q:
                    y, x = q.popleft()   # 방문
                    visited[y][x] = True   # 방문 처리
                    empty.append((y,x))
                    for dy, dx in directions:
                        if (0 <= y + dy < n) and (0 <= x + dx < n):
                            if game_board[y+dy][x+dx] == 0 and not visited[y+dy][x+dx]:
                                if (y+dy, x+dx) not in q:
                                    q.append((y+dy, x+dx))
                empty_list.append(empty)
                
    '''
    block_list와 empty_list를 구할 때, set()을 해주지 않으면, 2x2 정사각형 모양을 처리할 수 없다.
    이 방식은 방문하기 전까진 방문 체크를 하지 않고 추가하기 때문에, 중복돼서 추가된다.
    이를 해결해주기 위해선
    1. block_list 처럼 set(block)을 해주거나
    2. empty_list 처럼 방문한 적 없거나, 방문 예정 목록에 있다면 추가를 해주지 않는 것으로 해결할 수 있다.
    '''
    
    # 비교
    for empty in empty_list:
        for block in block_list:
            if len(empty) != len(block):
                continue
            if check(empty, block):   # 둘이 모양이 같으면
                answer += len(block)
                print(block)
                block_list.remove(block)
                break   # block에 대해 empty에 채웠으면 그 block은 더 이상 계산에 쓰이지 않는다.
    
    return answer