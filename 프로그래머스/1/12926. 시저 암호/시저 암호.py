from string import ascii_lowercase

def solution(s, n):
    answer = ''
    lower_list = ascii_lowercase
    upper_list = [chr(num)   for num in range(65,91)]   # 'A' ~ 'Z'
    print(lower_list)
    print(upper_list)
    for c in s:
        if c in lower_list:
            idx = lower_list.find(c)
            idx = idx+n if idx+n < len(lower_list) else idx+n-26
            answer = ''.join([answer, lower_list[idx]])
        elif c.isupper():
            answer += chr(ord(c)+n) if ord(c)+n < 91 else chr(ord(c)+n-26)
        else:
            answer += ' '
    return answer