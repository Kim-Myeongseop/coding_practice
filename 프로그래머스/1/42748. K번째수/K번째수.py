def solution(array, commands):
    answer = []
    for command in commands:
        start, end, idx = command
        answer.append(sorted(array[start-1:end])[idx-1])
    return answer