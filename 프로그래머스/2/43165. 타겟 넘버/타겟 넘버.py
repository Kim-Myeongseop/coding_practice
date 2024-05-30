def solution(numbers, target):
    answer = 0
    pointers = [0 for _ in range(len(numbers))]
    while True:
        # 계산 및 확인
        value = 0
        for i in range(len(numbers)):
            if pointers[i] == 0:   # 더하기
                value += numbers[i]
            else:   # 빼기
                value -= numbers[i]
        if value == target:
            answer += 1
        
        # pointers 업데이트
        for i in range(len(pointers)):
            if pointers[i] == 0:
                pointers[i] = 1
                break
            else:
                pointers[i] = 0
        if pointers == [1]*len(numbers):
            break
    return answer