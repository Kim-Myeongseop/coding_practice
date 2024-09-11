# class Solution:
#     def minBitFlips(self, start: int, goal: int) -> int:
#         return sum(map(int, bin(start ^ goal)[2:]))

# 다른 풀이 1
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        cnt = 0
        while start or goal:
            if start%2 != goal%2:   # 같지 않으면 바꿔야한다.
                cnt += 1
            start = start//2
            goal = goal // 2
        return cnt