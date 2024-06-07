def isrightstr(s):
    result = 0
    for c in s:
        if c == '(':
            result += 1
        else:
            result -= 1
        
        if result < 0:
            return False
    return True

def solution(p):
    answer = ''
    if p == '':
        return p
    else:
        l_cnt, r_cnt = 0, 0
        u, v = '', ''
        for i in range(len(p)):
            if p[i] == '(':
                l_cnt += 1
            else:
                r_cnt += 1
            
            if l_cnt == r_cnt:
                u = p[:i+1]
                v = p[i+1:]
                break
                
        if isrightstr(u):
            u += solution(v)
        else:
            temp = '(' + solution(v) + ')'
            for i in range(1,len(u)-1):
                if u[i] == '(':
                    temp += ')'
                else:
                    temp += '('
            u = temp
    
    answer += u
    return answer