def solution(n):
    def hanoi(num, start, end, temp):
        if num == 1:
            return [[start,end]]
        
        # n개를 1에서 3으로 옮기려면, n-1개를 1에서 2로 옮겨야한다.
        answer = []
        answer.extend(hanoi(num-1, start, temp, end))
        answer.extend(hanoi(1, start, end, temp))
        answer.extend(hanoi(num-1, temp, end, start))
        
        return answer
            
    
    return hanoi(n, 1, 3, 2)