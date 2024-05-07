def solution(s):
    answer = []
    s = s[1:-1].split('},')
    # s.lstrip('{').rstrip('}').split('},{') 으로 더 편하게 할 수 있다.
    s.sort(key=lambda x: len(x))   # key에는 함수가 오기 때문에, key=len도 가능하다.
    s_len = len(s)
    
    answer.append(int(s[0].replace('{','').replace('}','')))
    for i in range(s_len-1):
        next_set = set(s[i+1].replace('{','').replace('}','').split(','))
        prev_set = set(s[i].replace('{','').replace('}','').split(','))
        diff_set = next_set - prev_set
        num = int(diff_set.pop())
        answer.append(num)
    return answer