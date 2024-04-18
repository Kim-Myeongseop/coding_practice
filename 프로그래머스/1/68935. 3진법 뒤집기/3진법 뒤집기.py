def solution(n):
    answer = 0
    num3 = []
    while n:
        num3.append(str(n%3))
        n = n//3
    num3 = ''.join(num3[::-1])
    
    for e, num in zip(range(len(num3)), num3):
        answer += 3**e * int(num)
    
    return answer