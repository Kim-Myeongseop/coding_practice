class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [i for i in range(n+1)]   # i 번째 문자까지 최소 extra characters를 저장
        word_set = set(dictionary)   # 중복 단어들 제거
        
        for r in range(1, n+1):
            dp[r] = dp[r-1] + 1   # dp[r-1]이 바뀌었으면 이를 반영해야한다.
            for l in range(r):
                if s[l:r] in word_set:   # l번째 문자 하나만 있는것과 l번째 문자 이후로 한 단어인 것은
                    dp[r] = min(dp[r], dp[l])   # dp[l] 입장에선 같다. 즉, dp[r]에 반영가능하다.
        return dp[n]