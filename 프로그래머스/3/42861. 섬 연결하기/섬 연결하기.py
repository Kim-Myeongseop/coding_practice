from heapq import heappush, heappop

def solution(n, costs):   # Prim
    answer = 0
    
    # 연결 그래프 그리기
    graph = {i:[] for i in range(n)}   # 노드에 대해 (연결된 노드, 비용) tuple을 list에 저장
    for cost in costs:
        graph[cost[0]].append((cost[1], cost[2]))
        graph[cost[1]].append((cost[0], cost[2]))
    
    # 그래프를 이용해서 연결 비용에 대한 최소 heap 구성 후, 시작 노드를 추가
    heap = []
    visited = [False for _ in range(n)]
    start = 0   # 시작 노드
    for node, weight in graph[start]:   # 시작 노드(0)에 연결된 노드와 가중치를 추가
        heappush(heap, (weight, start, node))   # 비용에 대해 최소 heap
    visited[start] = True
    
    # heap이 다 없어질 때 까지(즉, 전부 방문하여 원소를 더이상 추가할 수 없을 때 까지)
    while heap:
        weight, _, node = heappop(heap)   # start는 사용하지 않음
        if visited[node]:
            continue
        
        visited[node] = True   # 방문 처리
        answer += weight
        for new_node, new_weight in graph[node]:
            if not visited[new_node]:
                heappush(heap, (new_weight, node, new_node))
    return answer

# 다른 풀이 1 : Kruskal
# def solution(n, costs):
#     # 다 연결만 되면 되므로, 최소 간선은 반드시 n-1개이다.(이때가 최소 비용)
#     answer = 0
    
#     # 비용에 따라 오름차순으로 정렬
#     costs.sort(key=lambda x: x[2])
    
#     # 모든 노드가 추가될 때 까지 추가한다.(초기값을 넣기 때문에 자연스럽게 n-1개의 간선이 추가된다.)
#     visited = set()
#     visited.add(costs[0][0])   # 첫번째 노드를 초기값으로 하여 시작
#     while len(visited) < n:
#         for cost in costs:   # 최소 비용의 간선부터 확인
#             # len(set(cost[:2]) & visited) == 1 으로 더 간단히 구할 수 있다.
#             if cost[0] in visited and cost[1] in visited:   # 둘다 이미 포함되었으면,
#                 continue   # 중복하여 추가하면 사이클을 형성하게된다. 따라서 pass
#             if cost[0] in visited or cost[1] in visited:   # 둘 중 하나만 포함된다면,
#                 visited.update([cost[0], cost[1]])   # update 대상은 iterable이어야 한다.
#                 answer += cost[2]   # 두 노드가 추가될 때, 그 사이의 간선이 추가된다.
#                 break   # 하나라도 추가되면, 다음 노드 확인해야한다.
#     return answer

# # 다른 풀이 2 : Kruskal + Union-Find
# def find(root_list, node):
#     if root_list[node] != node:   # root node가 아니라면,
#         root_list[node] = find(root_list, root_list[node])   # update
#     return root_list[node]

# def union(root_list, node1, node2):
#     root1 = find(root_list, node1)
#     root2 = find(root_list, node2)
#     root_list[root2] = root1   # 일반적으로 작은 값이 먼저 오기 때문에, 작은 값을 root로 보내자.
    
# def solution(n, costs):
#     answer = 0
#     root_list = [i for i in range(n)]   # root 노드를 가리키는 list
    
#     # 비용에 따라 오름차순으로 정렬
#     costs.sort(key=lambda x: x[2])
    
#     # 비용이 작은 섬부터 연결 : 트리를 구성한다.
#     for node1, node2, cost in costs:
#         if find(root_list, node1) != find(root_list, node2):   # root가 다르면
#             union(root_list, node1, node2)
#             answer += cost   # 연결하면 비용 추가
#     return answer

