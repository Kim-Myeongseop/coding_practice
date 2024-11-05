def solution(number, k):
    answer = []
    # 순서는 유지해야하고, 앞에서부터 큰 수를 남기는 것이 핵심이다.
    for num in number:
        # 가장 큰 수 전까지 그리고 k개 만큼 뺄 때 까지 앞에서부터 빼내야한다.
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    # 내림차순으로 되어있어서 다 뺏는데 k가 0보다 크다면 뒤에서 부터 k개만큼 잘라야한다. 
    answer = answer[:len(answer) - k]
    return ''.join(answer)