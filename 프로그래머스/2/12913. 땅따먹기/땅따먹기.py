def solution(land):
    prev = [0, 0, 0, 0]
    for row in land:   # 한 줄 씩 가면서 이전 점수 기반으로 최고 점수 row를 만들어서 prev를 update
        for i in range(4):   # row의 index
            max_prev = 0
            for j in range(4):   # prev의 index : 하나의 i에 대해서 3개의 j 확인
                if i != j:
                    max_prev = max(max_prev, prev[j])
            row[i] = row[i] + max_prev   # row의 원소를 순차적으로 update
        prev = row   # 현재 row는 다음 번에 prev
    return max(prev)   # 마지막 prev의 최대값