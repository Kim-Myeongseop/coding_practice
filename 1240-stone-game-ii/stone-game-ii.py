class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        dp = {}

        def recursiveStoneGame(start, M):   # start index에서 1~2M개 까지 가져올 수 있을 때, best stones 합
            if start >= N:
                return 0
            
            # 전부 가져올 수 있으면 전부 가져오는 것이 무조건 이득
            if start + 2*M >= N:
                return sum(piles[start:])
            
            # memoization
            if (start, M) in dp:
                return dp[(start, M)]

            my_score = 0
            total_score = sum(piles[start:])
            # 내가 가져올 수 있는 경우의 수 중 가장 큰 경우의 수 구하기
            for x in range(1, 2*M+1):
                # 상대 턴으로 넘겨서 상대가 가져올 수 있는 best stones 합
                opponent_score = recursiveStoneGame(start+x, max(x, M))
                # 누군지에 관계 없이 start index 시점에서 가져올 수 있는 최고 점수(재귀함수라 최종까지 계산된 결과임)
                my_score = max(my_score, total_score - opponent_score)
            dp[(start, M)] = my_score   # memoization
            return my_score

        return recursiveStoneGame(0, 1)

# 다른 풀이 1
# class Solution:
#     def stoneGameII(self, piles: List[int]) -> int:
#         n = len(piles)
        
#         dp = [[0] * (n + 1) for _ in range(n)]
#         suffix_sum = [0] * n
#         suffix_sum[-1] = piles[-1]
        
#         for i in range(n - 2, -1, -1):
#             suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
#         for i in range(n - 1, -1, -1):
#             for m in range(1, n + 1):
#                 if i + 2 * m >= n:
#                     dp[i][m] = suffix_sum[i]
#                 else:
#                     for x in range(1, 2 * m + 1):
#                         dp[i][m] = max(dp[i][m], suffix_sum[i] - dp[i + x][max(m, x)])
        
#         return dp[0][1]