def solution(n, times):
    answer = []
    # 시간 자체를 변수로 예측하는 방법. 이분 탐색으로 최적 점을 찾자.
    l = 0
    r = max(times)*n
    while l < r:
        total_people = 0
        mid = (l+r)//2
        for time in times:
            total_people += mid//time
            
        if total_people >= n:
            r = mid
            answer.append(mid)
        else:
            l = mid + 1   # 이 경우 l, r이 연속으로 있다면, 답이 r일 경우 l이 r로 가버리지만 while 문이 돌아가지 않아 mid가 초기화 될 수 없다 따라서 return mid 대신 return l을 하는 것이 맞다.
    answer = min(answer)
    return answer