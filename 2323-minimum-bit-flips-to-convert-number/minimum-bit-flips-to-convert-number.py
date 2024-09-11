class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return sum(map(int, bin(start ^ goal)[2:]))