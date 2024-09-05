def solution(money):
    n = len(money)
    dp1 = [0 for _ in range(n-1)]
    dp2 = [0 for _ in range(n-1)]
    
    for i in range(n-1):
        if i < 1:
            dp1[i] = money[i]
        else:
            dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    
    for i in range(n-1):
        if i < 1:
            dp2[i] = money[i+1]
        else:
            dp2[i] = max(dp2[i-1], dp2[i-2] + money[i+1])
    
    return max(max(dp1), max(dp2))