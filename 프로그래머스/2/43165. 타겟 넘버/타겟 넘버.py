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

'''
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
'''
    
'''
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer
'''