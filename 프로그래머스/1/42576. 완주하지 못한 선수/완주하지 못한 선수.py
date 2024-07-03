def solution(participant, completion):
    people_dict = {}
    for p in participant:
        if people_dict.get(p):
            people_dict[p] += 1
        else:
            people_dict[p] = 1
    
    for p in completion:
        if people_dict[p] == 1:
            people_dict.pop(p)
        else:
            people_dict[p] -= 1
    
    answer = list(people_dict.keys())[0]
    return answer