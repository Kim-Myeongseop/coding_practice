class Solution:
    def makeGood(self, s: str) -> str:
        while True:
            prev_len = len(s)
            for i in range(len(s)-1):
                if i >= len(s)-1:
                    break
                if (s[i]!=s[i+1]) and (s[i].lower()==s[i+1] or s[i]==s[i+1].lower()):
                    s = ''.join([s[:i], s[i+2:]])
            if prev_len == len(s):
                break
        return s
            