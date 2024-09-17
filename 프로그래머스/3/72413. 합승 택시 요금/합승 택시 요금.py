# def solution(n, s, a, b, fares):   # Floyd Warshall
#     answer = float('inf')
#     # matrix 만들기(노드와 노드로 가는 최저 금액)
#     matrix = [[float('inf') for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         matrix[i][i] = 0
#     for fare in fares:
#         matrix[fare[0]-1][fare[1]-1] = fare[2]
#         matrix[fare[1]-1][fare[0]-1] = fare[2]
    
#     # 중간을 걸쳐 가는 경로가 더 작은 경우 초기화
#     for k in range(n):   # 중간 index가 가장 먼저 나와야한다.
#         for i in range(n):
#             for j in range(n):
#                 matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
#                 matrix[j][i] = matrix[i][j]
    
#     # 중간까지 가는 노드를 기준으로 search
#     for i in range(n):
#         answer = min(answer, matrix[s-1][i] + matrix[i][a-1] + matrix[i][b-1])
    
#     return answer

# 다른 풀이 1 : Dijkstra
from collections import deque

def solution(n, s, a, b, fares):
    INF = 1e+5 * 200 * 2
    answer = INF
    graph = [[] for _ in range(n)]   # 각 노드별로 (연결할 노드, 거리 또는 비용)를 list로 저장
    for n1, n2, fare in fares:
        graph[n1-1].append((n2-1, fare))
        graph[n2-1].append((n1-1, fare))
    for i in range(n):   # 이 부분을 반드시 추가해줘야한다.
        graph[i].append((i, 0))   # 같은 노드에서 같은 노드로 가는 비용이 0임을 추가해야한다.
    
    fare_lists = []   # 모든 노드에 대해 각 노드가 start 노드가 되었을 때의 fare_list를 저장
    for start in range(n):
        fare_list = [INF]*n   # start 노드 기준으로 해당 노드까지의 비용 list
        queue = deque()
        queue.append((start, 0))
        while queue:
            node, fare = queue.popleft()   # bfs
            
            if fare_list[node] < fare:   # dis 보다 작으면 이전 방식에서 최소 거리 발생
                continue
            
            for new_node, new_fare in graph[node]:
                if fare + new_fare < fare_list[new_node]:
                    fare_list[new_node] = fare + new_fare
                    queue.append((new_node, fare_list[new_node]))
            
        fare_lists.append(fare_list)
    
    for i in range(n):   # 같이 타고 가는 지점에 따라 계산
        # (s -> i) + (i -> a) + (i -> b)
        fare = fare_lists[s-1][i] + fare_lists[i][a-1] + fare_lists[i][b-1]
        if fare < answer:
            answer = fare    
    return answer

