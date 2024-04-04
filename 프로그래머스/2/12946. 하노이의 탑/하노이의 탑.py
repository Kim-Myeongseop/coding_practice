def solution(n):
    def hanoi(num, start, end, temp):   # 원판의개수, 시작기둥, 목표기둥, 경유기둥
        if num == 1:
            return [[start,end]]
        
        answer = []
        answer.extend(hanoi(num-1, start, temp, end))   # n-1개를 start에서 temp로 옮기기
        answer.extend(hanoi(1, start, end, temp))   # 가장 큰 원반을 start에서 end로 옮기기
        answer.extend(hanoi(num-1, temp, end, start))   # n-1개를 temp에서 end로 옮기기
        
        return answer
    
    return hanoi(n, 1, 3, 2)