def solution(n, edge):
    graph = {i:[] for i in range(1, n+1)}
    visited = [False for _ in range(n)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    stack = graph[1]
    visited[0] = True
    while stack:
        temp = []
        for node in stack:
            visited[node-1] = True
            for n in graph[node]:   # 2에 연결된 애들 중 
                if not visited[n-1] and n not in stack:   # 방문하지 않은 녀석 같은 순번에도 없는 애들
                    temp.append(n)
                    visited[n-1] = True
        if temp:
            answer = len(temp)
            stack = temp
        else:
            break
    return answer