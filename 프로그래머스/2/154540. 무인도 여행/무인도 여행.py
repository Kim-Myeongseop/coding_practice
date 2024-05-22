def solution(maps):
    answer = []
    M = len(maps)   # M행
    N = len(maps[0])   # N열
    direction_list = [(1,0), (0,1), (-1,0), (0,-1)]
    search_zone = [[False]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if search_zone[i][j] == False and maps[i][j] != 'X':   # count start
                total = 0   # 합 구하기
                queue = [(i,j)]   # 첫 search 대상 append
                while queue:
                    # search 대상 좌표 가져오기
                    r = queue[0][0]
                    c = queue[0][1]
                    
                    # 값 확인 후 추가
                    if search_zone[r][c] == False and maps[r][c] != 'X':
                        total += int(maps[r][c])
                        search_zone[r][c] = True
                    
                        # 4방향 중 유효한 범위 좌표 queue에 추가
                        for dr, dc in direction_list:
                            if 0<=r+dr<M and 0<=c+dc<N:   # 둘 중 하나라도 밖이면 없는 좌표
                                if search_zone[r+dr][c+dc] == False and maps[r+dr][c+dc] != 'X':
                                    queue.append((r+dr, c+dc))
                    
                    # queue 삭제 : pop은 원소가 없으면 error가 발생하지만 이 문제에선 그런 경우가 없다.
                    queue.pop(0)   # queue = queue[1:]
                    # queue = queue[1:]
                
                # total 값 추가    
                answer.append(total)
    
    answer.sort()
    return answer if answer else [-1]