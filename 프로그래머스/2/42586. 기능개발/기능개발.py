import math

def solution(progresses, speeds):
    answer = []
    remain = []
    for i in range(len(progresses)):
        remain.append(math.ceil((100-progresses[i]) / speeds[i]))

    while remain:
        curr = remain.pop(0)
        temp = 1
        while remain and curr >= remain[0]:
            remain.pop(0)
            temp += 1
        answer.append(temp)
    return answer