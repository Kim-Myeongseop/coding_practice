import sys
sys.setrecursionlimit(10**6)   # 1e+6 표현이 안됨

def solution(n):
    dp = {}
    def fibo(n):
        if n < 2:
            dp[n] = n
            return n
        
        if dp.get(n-1):
            a = dp[n-1]
        else:
            a = fibo(n-1)
            dp[n-1] = a
        if dp.get(n-2):
            b = dp[n-2]
        else:
            b = fibo(n-2)
            dp[n-2] = b
        return a + b
    return fibo(n)%1234567