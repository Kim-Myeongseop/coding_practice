def solution(citations):
    answer = 0
    max_num = max(citations)
    for h in range(max_num):
        cnt = 0
        for citation in citations:
            if citation >= h:
                cnt += 1
        if cnt >= h:
            if h > answer:
                answer = h
    return answer