def solution(distance, rocks, n):
    if len(rocks) == n:   # 모든 돌 제거 경우의 수 배제
        return distance
    
    # linked
    '''
    start와 distance를 추가했다고 생각하고
    왼쪽부터 나아가므로(i는 0부터 오름차순)
    i번째 기준으로 i+1 번째 까지의 거리가 mid 미만이라면 i+1을 지우는 방법을 선택하면
    양쪽이 다 mid 미만인 돌을 우선으로 제거할 수 있음(양쪽 다 mid 미만이 아니더라도 먼저 제거해도 문제없음)
    '''
    linked = {}
    for i in range(len(rocks)):
        if i == 0:
            rocks.sort()
            linked[0] = ['Start', rocks[i]]
            linked[rocks[i]] = [0, rocks[i+1]]
        elif i == len(rocks)-1:
            linked[distance] = [rocks[i], 'End']
            linked[rocks[i]] = [rocks[i-1], distance]
        else:
            linked[rocks[i]] = [rocks[i-1], rocks[i+1]]
            
    l = 0
    r = distance
    while l < r:
        mid = (l+r)//2
        cnt = 0
        linked_copy = {k:v[:] for k, v in linked.items()}   # 반드시 v[:] 해줘야한다.
        for rock in rocks:
            left = linked_copy[rock][0]
            right = linked_copy[rock][1]
            if rock - left < mid:
                linked_copy[left][1] = right
                linked_copy[right][0] = left
                linked_copy[rock] = None   # 없는 돌
                cnt += 1

        if cnt > n:
            r = mid
        else:
            l = mid + 1
            answer = mid
    
    # answer = distance
    # for rock in rocks:
    #     if linked_copy[rock]:
    #         answer = min(answer, rock - linked_copy[rock][0])
    return answer

def solution(distance, rocks, n):
    if len(rocks) == n:   # 모든 돌 제거 경우의 수 배제
        return distance
    
    rocks.sort()  # 바위 위치를 미리 정렬합니다.
    
    # linked 딕셔너리 생성
    linked = {}
    linked[0] = ['Start', rocks[0]]
    for i in range(len(rocks)):
        if i == 0:
            linked[rocks[i]] = [0, rocks[i+1] if i+1 < len(rocks) else distance]
        elif i == len(rocks)-1:
            linked[distance] = [rocks[i], 'End']
            linked[rocks[i]] = [rocks[i-1], distance]
        else:
            linked[rocks[i]] = [rocks[i-1], rocks[i+1]]
            
    l = 1  # 최소 거리는 1부터 시작
    r = distance
    answer = 0
    while l <= r:  # 등호를 추가하여 모든 경우를 검사합니다.
        mid = (l+r)//2
        cnt = 0
        prev = 0
        for rock in rocks + [distance]:
            if rock - prev < mid:
                cnt += 1
            else:
                prev = rock
            if cnt > n:
                break
        
        if cnt > n:
            r = mid - 1
        else:
            l = mid + 1
            answer = mid  # 가능한 경우 중 최대값을 저장합니다.
    
    return answer