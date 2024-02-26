import math
def solution(n, s):
    if n > s:
        return [-1]
    
    c = math.floor(s/n)
    answer = [c]*n
    diff = s - sum(answer)
    print(diff)
    for i in range(diff):
        answer[n-1-i] += 1

    return answer