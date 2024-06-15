def solution(n, t, m, p):
    answer = ''
    number_list = '0123456789ABCDEF'[:n]   # 예를 들어 n == 3
    number = 0
    cnt = 0
    while len(answer) < t:
        num = number
        temp = []
        if num == 0:
            temp.append(str(num))
        while num > 0:
            temp.append(number_list[num%n])   # 숫자를 number_list에서 불러오기
            num = num//n
        temp = temp[::-1]
        for c in temp:
            if cnt == p-1:
                answer = answer + c
            cnt += 1
            if cnt == m:
                cnt = 0
        number += 1
    return answer[:t]