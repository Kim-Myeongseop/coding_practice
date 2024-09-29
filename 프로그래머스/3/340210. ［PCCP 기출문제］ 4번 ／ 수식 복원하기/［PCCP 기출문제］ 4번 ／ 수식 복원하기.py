def to_Base_N(num, base):   # 10진법 수 -> n진법 수
    if num == 0:
        return str(0)
    temp = []
    while num:
        temp.append(str(num%base))
        num = num // base
    return ''.join(temp[::-1])

def solution(expressions):
    answer = []
    n_list = [n for n in range(2,10)]   # 진법 리스트
    questions = []   # "X"가 포함된 식 리스트
    
    # 가능한 진법만 남기기
    for expression in expressions:
        a, operator, b, _, c = expression.split()
        maximum = int(max(list(a + b + c.replace('X', ''))))   # 식에서 나오는 가장 큰 숫자 저장
        for n in n_list:
            if n > maximum:
                idx = n_list.index(n)
                break
        n_list = n_list[idx:]   # maximum 이하의 숫자들은 고려 대상이 아니다.
        if c == 'X':   # questions에 추가하고, 추론에는 사용하지 않는다.
            questions.append(expression)
            continue
        
        # 진법 리스트에 숫자들을 이용해서 해당 식을 만족하지 않는 숫자는 진법 리스트에서 제거
        del_list = []
        if operator == '+':
            for n in n_list:
                if int(a, n) + int(b, n) != int(c, n):
                    del_list.append(n)
        else:   # '-'
            for n in n_list:
                if int(a, n) - int(b, n) != int(c, n):
                    del_list.append(n)
        # 진법 리스트에서 제거
        for n in del_list:
            if n in n_list:
                n_list.remove(n)
    
    # 가능한 진법들을 통해 계산(하나라도 일치하지않는 계산식의 결과는 "?")
    for expression in questions:
        a, operator, b, _, c = expression.split()
        # class.method(self, **args) 방식
        operator = int.__add__ if operator == '+' else int.__sub__
        
        result = False
        for n in n_list:
            if to_Base_N(operator(int(a, n), int(b, n)), n) != result:
                if result is False:   # False == 0 은 True이다.
                    result = to_Base_N(operator(int(a, n), int(b, n)), n)
                else:
                    result = "?"
                    break
        answer.append(expression.replace("X", str(result)))
    return answer