from collections import deque

def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    directions = [[1,0], [0,1], [-1,0], [0,-1]]
    
    queue = deque()
    queue.append((0,0))   # row, column, distance
    visited = [[10000 for _ in range(m)] for _ in range(n)]   # 10000은 방문 전
    visited[0][0] = 1
    while queue:
        row, col = queue.popleft()   # bfs
        dist = visited[row][col]
        for dy, dx in directions:
            if 0 <= row+dy < n and 0 <= col+dx < m:
                if maps[row+dy][col+dx] == 1 and visited[row+dy][col+dx] > dist + 1:
                    visited[row+dy][col+dx] = dist + 1
                    queue.append((row+dy, col+dx))
                    if row+dy == n-1 and col+dx == m-1:
                        answer = visited[row+dy][col+dx]
                        break
    return answer