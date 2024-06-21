def solution(n, times):
    answer = []
    # 시간 자체를 변수로 예측하는 방법. 이분 탐색으로 최적 점을 찾자.
    l = 0
    r = max(times)*n
    while l <= r:
        total_people = 0
        mid = (l+r)//2
        for time in times:
            total_people += mid//time
            
        if total_people >= n:
            r = mid - 1
            answer.append(mid)
        else:
            l = mid + 1
    answer = min(answer)
    return answer