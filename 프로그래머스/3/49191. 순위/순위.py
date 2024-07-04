def solution(n, results):
    answer = 0
    graph = {p:[[],[]] for p in range(1, n+1)}   # 나보다 위의 리스트, 나보다 아래 리스트
    for win, lose in results:
        graph[win][1].append(lose)
        graph[lose][0].append(win)
    
    for p in graph:
        # 나보다 등수 높은 사람 조회
        win_list = []
        visited = {}
        stack = graph[p][0][:]
        while stack:
            visit = stack.pop()
            win_list.append(visit)
            for q in graph[visit][0]:
                if not visited.get(q):
                    visited[q] = True
                    stack.append(q)
        
        # 나보다 등수 낮은 사람 조회
        lose_list = []
        visited = {}
        stack = graph[p][1][:]
        while stack:
            visit = stack.pop()
            lose_list.append(visit)
            for q in graph[visit][1]:
                if not visited.get(q):
                    visited[q] = True
                    stack.append(q)
        
        # 최종 수 확인
        if len(set(win_list)) + len(set(lose_list)) == n-1:
            answer += 1
    return answer

# 다른 풀이 1
'''
from collections import defaultdict
win, lose = defaultdict(set), defaultdict(set)   # value의 default를 set으로 하는 dict 생성
# set의 method인 add(원소 추가), remove(원소 삭제), update(원소들 추가) 를 이용해서 풀이
'''