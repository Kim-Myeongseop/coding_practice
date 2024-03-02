class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split().pop())   # split(' ')를 하면 '' 들도 output으로 포함해서 분리함
        