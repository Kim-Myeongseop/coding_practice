def solution(n):
    answer = []
    
    tower = [[0]*i   for i in range(1, n+1)]
    r, c = 0, 0
    
    direction = [(1,0), (0,1), (-1,-1)]
    d_idx = 0
    
    total = n*(n+1)//2
    for num in range(1, total+1):
        # 할당 : 무조건 num은 하나 할당해야 끝난다.
        tower[r][c] = num
        # if tower[r][c] == 0:
        #     tower[r][c] = num
        # else:   # num은 무조건 할당해야하고 방향은 1번만 바뀐다.
        #     d_idx = d_idx+1 if d_idx != 2 else 0
        #     r += direction[d_idx][0]
        #     c += direction[d_idx][1]
        #     tower[r][c] = num
        
        # 다음 인덱스 부여 : 문제 발생시 방향전환필요
        r += direction[d_idx][0]
        c += direction[d_idx][1]
        
        if r>=n or c>r or tower[r][c]!=0:   # r>=n 임에 주의 / 다음 포인트가 0이 아니면 다시
            r -= direction[d_idx][0]
            c -= direction[d_idx][1]
            d_idx = d_idx+1 if d_idx !=2 else 0
            r += direction[d_idx][0]
            c += direction[d_idx][1]
    
    for line in tower:
        for num in line:
            answer.append(num)
    
    return answer