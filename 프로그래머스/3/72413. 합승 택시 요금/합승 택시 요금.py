def solution(n, s, a, b, fares):
    answer = float('inf')
    # matrix 만들기(노드와 노드로 가는 최저 금액)
    matrix = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 0
    for fare in fares:
        matrix[fare[0]-1][fare[1]-1] = fare[2]
        matrix[fare[1]-1][fare[0]-1] = fare[2]
    
    # 중간을 걸쳐 가는 경로가 더 작은 경우 초기화
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                matrix[j][i] = matrix[i][j]
    
    # 중간까지 가는 노드를 기준으로 search
    for i in range(n):
        answer = min(answer, matrix[s-1][i] + matrix[i][a-1] + matrix[i][b-1])
    
    return answer