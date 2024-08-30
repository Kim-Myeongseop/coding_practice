def solution(triangle):
    sum_list = []
    for i in range(len(triangle)):
        temp = []
        for j in range(len(triangle[i])):
            if i == 0:
                prev_num = 0
            else:
                if j == 0:   # 가장 왼쪽 값 : 선택할 수 있는 경우의 수 1개
                    prev_num = sum_list[i-1][j]
                elif j == i:   # 가장 오른쪽 값 : 선택할 수 있는 경우의 수 1개
                    prev_num = sum_list[i-1][j-1]
                else:   # 중간 : 2개 중 큰 값 선택
                    prev_num = max(sum_list[i-1][j-1], sum_list[i-1][j])
            temp.append(triangle[i][j] + prev_num)
        sum_list.append(temp)
    return max(temp)

'''
위에서 부터 가능한 최대값을 아래 수로 더해줌
7 / 3 8 / 8 1 0 -> 10 15 / 8 1 0 -> 18 16 15
즉, 현재 row의 값들까지 오는 경로 중 최대값으로 교체하는 것
'''