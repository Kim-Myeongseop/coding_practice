def solution(stones, k):
    answer = 1
    l = 1
    r = max(stones)
    while l <= r:
        mid = (l+r)//2
        cnt = 0
        for stone in stones:
            if stone < mid:
                cnt += 1
            else:
                cnt = 0
            
            if cnt >= k:
                break
        
        if cnt >= k:
            r = mid - 1
        else:
            answer = mid
            l = mid + 1
    return answer

'''
돌을 밟을 수 있으면 무조건 밟힌다.
즉, 카운트 될 수 있는데 카운트가 안되는 경우는 없다.
숫자가 매우 크니 이분 탐색으로 answer를 찾아보자
'''