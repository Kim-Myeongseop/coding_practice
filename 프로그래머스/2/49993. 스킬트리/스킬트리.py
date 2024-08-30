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