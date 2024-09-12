def solution(n):
    answer = 0
    n = bin(n)[2:]
    for i in n:
        if i == '1':
            answer += 1
    return answer