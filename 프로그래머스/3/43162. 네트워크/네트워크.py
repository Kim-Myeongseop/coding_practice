def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:   # 방문 전이면 count
            stack = [i]
            while True:
                temp = 0
                for j in range(n):
                    if i != j and visited[j] == False:
                        for s in stack:
                            if computers[j][s] == 1 and j not in stack:
                                stack.append(j)
                                temp += 1
                                visited[j] = True
                if temp == 0:
                    break
            answer += 1
    return answer