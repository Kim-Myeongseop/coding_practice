from collections import deque

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        answer = 0
        n = len(grid)
        board = [[0]*3*n for _ in range(3*n)]   # 0이면 방문 전, 1이면 방문 또는 벽
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == '/':
                    board[3*r][3*c+2] = 1
                    board[3*r+1][3*c+1] = 1
                    board[3*r+2][3*c] = 1
                elif grid[r][c] == "\\":
                    board[3*r][3*c] = 1
                    board[3*r+1][3*c+1] = 1
                    board[3*r+2][3*c+2] = 1
        
        for r in range(3*n):
            for c in range(3*n):
                if board[r][c] == 0:
                    answer += 1
                    queue = deque()
                    queue.append((r,c))
                    while queue:
                        visit = queue.popleft()
                        board[visit[0]][visit[1]] = 1   # 방문 처리
                        for y, x in directions:
                            ny = visit[0] + y
                            nx = visit[1] + x
                            if 0 <= ny < 3*n and 0 <= nx < 3*n:
                                if board[ny][nx] == 0 and (ny, nx) not in queue:
                                    queue.append((ny, nx))
        return answer

# 다른 풀이 1
# class Solution:
#     def regionsBySlashes(self, grid: List[str]) -> int:
#         def find(x):
#             if p[x] != x:
#                 p[x] = find(p[x])
#             return p[x]

#         def union(a, b):
#             pa, pb = find(a), find(b)
#             if pa != pb:
#                 p[pa] = pb
#                 nonlocal size
#                 size -= 1

#         n = len(grid)
#         size = n * n * 4
#         p = list(range(size))
#         for i, row in enumerate(grid):
#             for j, v in enumerate(row):
#                 k = i * n + j
#                 if i < n - 1:
#                     union(4 * k + 2, (k + n) * 4)
#                 if j < n - 1:
#                     union(4 * k + 1, (k + 1) * 4 + 3)
#                 if v == '/':
#                     union(4 * k, 4 * k + 3)
#                     union(4 * k + 1, 4 * k + 2)
#                 elif v == '\\':
#                     union(4 * k, 4 * k + 1)
#                     union(4 * k + 2, 4 * k + 3)
#                 else:
#                     union(4 * k, 4 * k + 1)
#                     union(4 * k + 1, 4 * k + 2)
#                     union(4 * k + 2, 4 * k + 3)
#         return size