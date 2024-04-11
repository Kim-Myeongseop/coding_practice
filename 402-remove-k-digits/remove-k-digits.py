import sys
sys.set_int_max_str_digits(100000)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and stack[-1]>n and k>0:   # 제거 조건
                stack.pop()
                k -= 1
            stack.append(n)
        stack = ''.join(stack)
        stack = stack[:len(stack)-k]
        return str(int(stack)) if stack else '0'

