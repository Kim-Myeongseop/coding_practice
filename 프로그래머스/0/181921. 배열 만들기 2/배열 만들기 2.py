def solution(l, r):
    answer = []
    for i in '05':
        for j in '05':
            for k in '05':
                for h in '05':
                    for m in '05':
                        for n in '05':
                            x = int(i + j + k + h + m + n)
                            if x == 0 or x < l:
                                continue
                            if x <= r:
                                answer.append(x)
                            else:
                                return answer if answer else [-1]
    return answer if answer else [-1]