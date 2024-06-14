def solution(numbers):
    answer = []
    numbers = sorted(map(str, numbers), reverse=True)
    for number in numbers:
        temp = []
        while answer and answer[-1] + number < number + answer[-1]:
            temp.append(answer.pop())
        answer.append(number)
        while temp:
            answer.append(temp.pop())
    answer = ''.join(answer)
    return str(int(answer))