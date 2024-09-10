def solution(k, tangerine):
    count_dict = {}
    for t in tangerine:
        count_dict[t] = count_dict.get(t, 0) + 1
    
    tangerine.sort(key=lambda x: (count_dict[x], x), reverse=True)
    cnt = 0
    answer = len(set(tangerine[:k]))
    return answer