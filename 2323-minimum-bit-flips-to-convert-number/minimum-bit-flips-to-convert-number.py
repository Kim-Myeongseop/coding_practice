class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        answer = start ^ goal
        answer = bin(answer)[2:]
        return sum(map(int, answer))