def solution(diffs, times, limit):
    answer = 0
    n = len(diffs)
    l = 1   # 최저 level
    r = 2 * max(diffs)   # 최고 level
    while l < r:
        level = (l+r)//2
        total = times[0]
        for i in range(1, n):
            total += times[i]
            if diffs[i] > level:
                total += (diffs[i] - level) * (times[i] + times[i-1])
        
        if total <= limit:
            r = level
            answer = r
        else:
            l = level + 1
    return answer