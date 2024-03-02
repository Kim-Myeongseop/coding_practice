class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split()   # split(' ')를 하면 '' 들도 output으로 포함해서 분리함
        return len(s_list[-1])