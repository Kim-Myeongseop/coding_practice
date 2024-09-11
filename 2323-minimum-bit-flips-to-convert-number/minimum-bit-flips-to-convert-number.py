class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        cnt = 0
        while start or goal:
            if start%2 != goal%2:
                cnt += 1
            start = start//2
            goal = goal // 2
        return cnt