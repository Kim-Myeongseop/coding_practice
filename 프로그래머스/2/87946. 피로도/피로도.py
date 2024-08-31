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