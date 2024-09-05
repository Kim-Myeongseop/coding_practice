def solution(money):
    n = len(money)
    # 0번째와 n번째 집 중 하나는 무조건 버려야되기 때문에 0 ~ n-2, 1 ~ n-1 두 경우의 수를 조회하자
    dp1 = [0 for _ in range(n)]   # (0번째 집 ~ n-2번째 집)
    dp2 = [0 for _ in range(n)]   # (1번째 집 ~ n-1번째 집)
      
    # 0번째 집 ~ n-2번째 집
    for i in range(n-1):
        if i == 0:
            dp1[i] = money[i]
        elif i == 1:
            dp1[i] = max(money[i], money[i-1])
        else:
            dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    
    # 1번째 집 ~ n-1번째 집
    for i in range(1, n):
        if i == 1:
            dp2[i] = money[i]
        elif i == 2:
            dp2[i] = max(money[i], money[i-1])
        else:
            dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    return max(max(dp1), max(dp2))

'''
dp를 i번째 집까지 털었을 때, 얻을 수 있는 최대 금액이라고 한다면, i-1번째와 i-2번째만 확인하면 된다.
1개까지의 최대값은 무조건 1번 집, 2개까지의 최대값은 1번 집 2번 집 중 큰 집.
집이 3개 있을 때, 1번 값과 3번 값의 합과 2번의 값 중 큰 값이 3개의 집을 털어서 얻을 수 있는 최대 금액이다.
'''