def solution(N, number):
    answer = -1
    dp = {i:{int(str(N)*i)} for i in range(1, 9)}   # 해당 횟수로 만들 수 있는 숫자를 set에 모은다.

    if N == number:
        return 1
    
    for i in range(2, 9):   # 1번에 만들 수 있는 숫자는 N 뿐이고 이미 구해놨다.
        for j in range(1, i):   # i번으로 만들 수 있는 수 : j + (i-j)
            for num1 in dp[j]:   # j번으로 만들 수 있는 숫자들
                for num2 in dp[i-j]:   # (i-j)번으로 만들 수 있는 숫자들
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
        
        if number in dp[i]:
            answer = i
            break
    
    return answer