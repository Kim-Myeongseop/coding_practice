def compute(operator, target):
        idx = 0
        while operator in target:
            for i in range(len(target)):
                if target[i] == operator:
                    target[i-1:i+2] = [str(eval(f"({target[i-1]}) {target[i]} ({target[i+1]})"))]
                    break
        return target

def solution(expression):
    answer = 0
    operators = ['*', '+', '-']
    operators = [operator for operator in operators if operator in expression]
    orders = []
    if len(operators) == 3:
        items = ["012", "021", "102", "120", "201", "210"]
        for item in items:
            i, j, k = int(item[0]), int(item[1]), int(item[2])
            orders.append([operators[i], operators[j], operators[k]])
    elif len(operators) == 2:
        items = ["01", "10"]   
        for item in items:
            i, j = int(item[0]), int(item[1])
            orders.append([operators[i], operators[j]])
    else:
        return abs(eval(expression))

    compute_list = []
    pointer = 0
    while expression:   # computer_list 로 만들기
        if expression[pointer] in operators:
            compute_list.append(expression[:pointer])
            compute_list.append(expression[pointer])
            expression = expression[pointer+1:]
            pointer = 0
        else:
            pointer += 1
        
        if pointer >= len(expression)-1:
            compute_list.append(expression)
            break
    
    for order in orders:   # 우선순위 종류에 따라 계산값 구하기
        target = [item for item in compute_list]
        for operator in order:
            target = compute(operator, target)
        target = abs(int(target[0]))
        if target > answer:
            answer = target
    
    return answer