def solution(s):
    answer = True
    nums = '0123456789'
    if len(s) == 4 or len(s) == 6:
        for c in s:
            if c in nums:
                continue
            else:
                answer = False
                break
    else:
        answer = False
    return answer