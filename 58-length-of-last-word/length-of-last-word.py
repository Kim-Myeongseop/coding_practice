class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split(' ')
        for i in range(1, len(s_list)+1):
            if len(s_list[-i]) > 0:
                result = len(s_list[-i])
                break
        return result