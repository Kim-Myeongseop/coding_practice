from heapq import heappush, heappop

def solution(jobs):
    jobs.sort()
    n = len(jobs)   # 총 길이
    cnt = 0   # 처리 개수
    total = 0   # 소요 시간의 합
    
    wait_list = []   # 대기 중인 작업 list : heapq argument must be a list
    now = 0   # 현재 시각
    
    # 소요 시간이 짧을 수록, 먼저 처리하면 이득이므로, 소요 시간을 기준으로 최소 힙을 구성하자.
    while cnt < n:   # cnt는 작업이 완료될 때 ++
        # 작업이 시작되면, now가 그 작업의 종료 시점으로 업데이트 되므로, 그 전까지의 작업은 wait_list에 추가
        while jobs and now >= jobs[0][0]:   # [요청 시간, 소요 시간]
            process = jobs.pop(0)
            heappush(wait_list, (process[1], process[0]))   # 소요 시간 기준으로 최소 힙
        
        # 공백이 발생해, jobs는 남아있는데, wait_list는 비어있는 경우 추가해주는 작업
        if jobs and not wait_list:
            process = jobs.pop(0)
            now = process[0]
            heappush(wait_list, (process[1], process[0]))
        
        # process 처리
        x, y = heappop(wait_list)   # 첫 번째 값이 소요 시간이다.
        now += x
        total += now - y   # 현재 시각(작업 종료 시간) - 요청 시간
        cnt += 1
        
    return total // cnt