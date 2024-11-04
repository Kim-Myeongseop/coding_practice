def solution(people, limit):
    answer = 0
    people.sort()
    l = 0
    r = len(people) - 1
    while l <= r:
        if people[l] + people[r] <= limit:   # limit 이하이면 둘 다 구출
            l += 1
            r -= 1
        else:   # 현재 가장 작은 사람과도 짝 지을 수 없는 사람은 혼자 구출해야만 한다.
            r -= 1
        answer += 1
    return answer