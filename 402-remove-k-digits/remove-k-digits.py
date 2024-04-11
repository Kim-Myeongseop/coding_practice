import sys
sys.set_int_max_str_digits(100000)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k>0 and stack and stack[-1]>n:   # 제거 조건(k가 0이되면 그 뒤로는 확인을 안해서 맨 앞)
                stack.pop()
                k -= 1
            stack.append(n)
        stack = stack[:len(stack)-k]
        stack = ''.join(stack)
        return str(int(stack)) if stack else '0'

