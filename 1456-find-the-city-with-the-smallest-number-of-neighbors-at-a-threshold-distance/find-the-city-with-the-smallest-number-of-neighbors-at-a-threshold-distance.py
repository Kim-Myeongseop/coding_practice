class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # 각 도시 별로 거리 내에 도달할 수 있는 도시의 개수를 구하고
        # 도달할 수 있는 도시의 수가 가장 적은 도시를 구한다.
        # 이때, 도시가 여러개면 가장 큰 값을 return한다.
        graph = [[10**6]*n for _ in range(n)]
        for edge in edges:
            graph[edge[0]][edge[1]] = edge[2]
            graph[edge[1]][edge[0]] = edge[2]
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist = graph[i][k] + graph[k][j]
                    if graph[i][j] > dist:
                        graph[i][j] = dist
                        graph[j][i] = dist
        
        minimum = n
        for i in range(n):
            cnt = 0
            for j in range(n):
                if i == j:
                    continue
                if graph[i][j] <= distanceThreshold:
                    cnt += 1
            if cnt <= minimum:
                minimum = cnt
                answer = i
        return answer