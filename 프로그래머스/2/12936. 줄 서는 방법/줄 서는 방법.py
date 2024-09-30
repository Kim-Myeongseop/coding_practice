def solution(n, k):
    answer = []
    arr = [i for i in range(1,n+1)]
    total = 1
    for i in range(1, n):
        total *= i
    
    while total > 0:
        idx = (k-1) // (total)   # (n-1)!, (n-2)! 으로 나눴을 때의 몫+1 번째 파티션으로 나누기 위해
        answer.append(arr.pop(idx))
        k %= total   # 나머지가 이제 새로운 파티션에서 몇 번째 숫자에 해당하는지가 된다.
        n -= 1   # for문 보다 더 빠르다.
        if n == 0:   # n이 0이 되면 0으로 나누기 전에 방지
            break
        total //= n
    return answer
    
    '''
    n, k = 5, 33
    total = 4 * 3 * 2 * 1
    n = 5
    1을 빼고 total으로 나눈 몫이 남은 arr의 idx
    ex) 33번째 수
    33 = 24 * (1) + 6 * (1) + 2 * (1) + 1 * (0) + 0 * (1)
    '''