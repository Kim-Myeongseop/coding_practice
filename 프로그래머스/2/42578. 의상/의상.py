def solution(clothes):
    hash_table = {}
    for name, category in clothes:
        if hash_table.get(category):
            hash_table[category] += 1
        else:
            hash_table[category] = 1
    answer = 1
    for key in hash_table:
        answer *= hash_table[key]+1
    return answer - 1