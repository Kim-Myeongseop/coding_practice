def solution(n, s, a, b, fares):   # Floyd Warshall
    answer = float('inf')
    # matrix 만들기(노드와 노드로 가는 최저 금액)
    matrix = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 0
    for fare in fares:
        matrix[fare[0]-1][fare[1]-1] = fare[2]
        matrix[fare[1]-1][fare[0]-1] = fare[2]
    
    # 중간을 걸쳐 가는 경로가 더 작은 경우 초기화
    for k in range(n):   # 중간 index가 가장 먼저 나와야한다.
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                matrix[j][i] = matrix[i][j]
    
    # 중간까지 가는 노드를 기준으로 search
    for i in range(n):
        answer = min(answer, matrix[s-1][i] + matrix[i][a-1] + matrix[i][b-1])
    
    return answer

# 다른 풀이 1 : Dijkstra
# from collections import deque

# def solution(n, s, a, b, fares):
#     answer = 0
#     INF = 1e+5 * 200 * 2
#     graph = [[] for _ in range(n)]   # 각 노드별로 (연결할 노드, 거리 또는 비용)를 list로 저장
#     for n1, n2, fare in fares:
#         graph[n1-1].append((n2-1, fare))
#         graph[n2-1].append((n1-1, fare))
    
#     distance = [INF]*n
#     queue = deque()
#     queue.append((start, 0))

    # return answer

