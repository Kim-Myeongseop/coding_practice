from collections import deque

def solution(prices):
    n = len(prices)
    answer = [n-1-i for i in range(n)]
    for i in range(1, n):
        idx = i - 1
        while idx >= 0 and prices[idx] > prices[i]:
            answer[idx] = min(answer[idx], i - idx)
            idx -= 1
    return answer