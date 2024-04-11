import sys
sys.set_int_max_str_digits(100000)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        cnt = 0 
        for n in num:
            while stack and stack[-1]>n and cnt<k:   # 제거 조건
                stack.pop()
                cnt += 1
            stack.append(n)
        stack = ''.join(stack)
        stack = stack[:len(num)-k]
        return str(int(stack)) if stack else '0'

