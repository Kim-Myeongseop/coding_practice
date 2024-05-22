def solution(priorities, location):
    answer = 0
    queue_len = len(priorities)   # location과 queue_len-1 을 pointer로 활용
    while priorities:
        # queue에서 원소를 하나 꺼낸다.
        process = priorities.pop(0)
        if not priorities:   # 길이가 0이면 마지막 process 이므로 answer 하나 추가하고 실행 후 종료
            answer += 1
            break
        location -= 1
        queue_len -= 1

        # 우선순위가 더 높으면(남은 queue의 최대값 이상이면) 실행
        # 길이가 매우 커지면, number가 9개 밖에 없으므로 dict로 index 관리하는 것도 더 빠를 듯 하다.
        if process >= max(priorities):   # process done
            answer += 1
            if location == -1:
                break
        else:   # process go to back of the queue
            priorities.append(process)
            queue_len += 1   # queue_len 다시 늘리기
            if location == -1:
                location = queue_len-1
                
    return answer