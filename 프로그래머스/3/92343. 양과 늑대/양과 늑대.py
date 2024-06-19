# 다음에는 메모이제이션 방법을 사용해보자.
# 방문 상태를 1000111010101 처럼 이진법으로 표현하고 값을 숫자로 저장.

from collections import deque
from itertools import permutations

def solution(info, edges):
    answer = 0
    
    # tree 만들기
    tree = {i:[-1, []] for i in range(len(info))}   # tree[node] = 부모, [자식들]
    for edge in edges:
        tree[edge[0]][1].append(edge[1])   # 자식 추가
        tree[edge[1]][0] = edge[0]   # 부모 추가
    
    # visit_path 만들기 : 양 node 기준으로 거슬러 올라가는 path만 의미있음
    visit_path = deque()
    for i in range(len(info)):
        if info[i] == 0:   # 양이고 & 자식 노드가 없거나 양이 없거나 => 이 경우만 추가
            tree[i][1]
            if not tree[i][1] or sum([info[n] for n in tree[i][1]])/len(tree[i][1]) == 1:
                visit = i
                temp = [i]
                while visit > 0:
                    temp.append(tree[visit][0])   # 부모 노드 추가
                    visit = tree[visit][0]   # 부모 노드 추가
                visit_path.append(temp[::-1])
    
    # visit_path 들의 모든 가능한 순열 만들기
    visit_path = permutations(visit_path)
    for total_path in visit_path:   # 여러 순서 중 하나(중복 되어 있는 상태)
        temp = []   # 최종 경로
        for path in total_path:
            for node in path:
                if node not in temp:
                    temp.append(node)
        # temp 경로에 대해 count
        sheep, wolf = 0, 0
        for node in temp:
            if info[node]:
                if sheep-1 > wolf:
                    wolf += 1
                else:
                    break
            else:
                sheep += 1
        if sheep > wolf:
            answer = max(answer, sheep)
    return answer
    