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
            linked[rocks[i]] = [rocks[i-1], distance]
            linked[distance] = [rocks[i], 'End']
        else:
            linked[rocks[i]] = [rocks[i-1], rocks[i+1]]
        
    l = 1
    r = distance
    while l <= r:
        mid = (l+r)//2
        cnt = 0
        linked_copy = {k:v[:] for k, v in linked.items()}   # 반드시 v[:] 해줘야한다.
        for rock in rocks:
            left, right = linked_copy[rock]
            if rock - left < mid:
                linked_copy[left][1] = right
                linked_copy[right][0] = left
                linked_copy[rock] = None   # 없는 돌
                cnt += 1
        if distance - linked_copy[distance][0] < mid:   # 도착지점 기준으로도 거리 계산해야함
            cnt += 1

        if cnt > n:
            r = mid - 1
        else:
            l = mid + 1
            answer = mid
    
    # mid가 실제로 돌과 돌 사이에 없는 거리일 수 있다.(이 부분이 없어도 돌아가는 이유를 모르겠다.)
    mid = answer
    linked_copy = {k:v[:] for k, v in linked.items()}   # 반드시 v[:] 해줘야한다.
    for rock in rocks:
        left, right = linked_copy[rock]
        if rock - left < mid:
            linked_copy[left][1] = right
            linked_copy[right][0] = left
            linked_copy[rock] = None   # 없는 돌
    
    d_list = []
    for rock in rocks + [distance]:
        if linked_copy[rock]:   # 돌이 있으면
            d = rock - linked_copy[rock][0]
            if d >= mid:
                d_list.append(d)
    answer = min(d_list)
    return answer