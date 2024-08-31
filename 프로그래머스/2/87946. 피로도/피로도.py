from collections import deque
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    temp = deque()
    for i in range(len(dungeons)):
        if dungeons[i][0] <= k:
            temp.append(dungeons[i])
    dungeons = temp
    
    for case in permutations(dungeons):
        temp = k
        cnt = 0
        for dungeon in case:
            if temp >= dungeon[0]:
                temp -= dungeon[1]
                cnt += 1
            if temp < 0:
                break
        answer = max(answer, cnt)
    return answer

# 다른 풀이 1
# answer = 0
# N = 0
# visited = []

# def dfs(k, cnt, dungeons):
#     global answer
#     if cnt > answer:
#         answer = cnt

#     for j in range(N):
#         if k >= dungeons[j][0] and not visited[j]:   # cnt를 추가할 수 있는 조건
#             visited[j] = 1   # 방문 처리
#             dfs(k - dungeons[j][1], cnt + 1, dungeons)   # cnt 추가 후 다음 단계 진행
#             visited[j] = 0   # 위의 탐색이 종료됐으면 다음 탐색을 위해 미방문 처리 후 for문 이어서

# def solution(k, dungeons):
#     global N, visited
#     N = len(dungeons)
#     visited = [0] * N
#     dfs(k, 0, dungeons)
#     return answer