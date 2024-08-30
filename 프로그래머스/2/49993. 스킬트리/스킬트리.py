def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        for s in skill_tree:
            if s not in skill:
                skill_tree = skill_tree.replace(s, '')
        
        sign = True
        for i in range(len(skill_tree)):
            if skill[i] != skill_tree[i]:
                sign = False
        if sign:
            answer += 1
    return answer

# 다른 풀이 1
# def solution(skill, skill_trees):
#     answer = 0
#     for skill_tree in skill_trees:
#         skill_list = list(skill)
#         for s in skill_tree:
#             if s in skill:
#                 if s != skill_list.pop(0):
#                     break
#         else:   # for문이 끝나기 전엔 두 번째 if문이 거짓이면 for문을 돈다.
#             answer += 1   # 그러다 for문이 다 돌때까지 한번도 일어나지 않으면, 마지막 if문은 else로 간다.
                    
#     return answer