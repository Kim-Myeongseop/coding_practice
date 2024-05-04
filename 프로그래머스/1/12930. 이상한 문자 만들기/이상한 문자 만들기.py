def solution(s):
    answer = ''
    idx = 0
    for c in s:
        if c == ' ':
            idx = 0
            answer += ' '
        else:
            answer = ''.join([answer, c.upper() if idx%2==0 else c.lower()])
            idx += 1
    return answer