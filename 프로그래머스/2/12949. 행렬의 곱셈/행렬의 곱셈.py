def solution(arr1, arr2):
    answer = [[0   for _ in range(len(arr2[0]))]   for _ in range(len(arr1))]
    # arr1   # m, n
    # arr2   # n, k
    for i in range(len(arr1)):   # 0~m-1
        for k in range(len(arr2[0])):

            for j in range(len(arr1[0])):   # 0~n-1
                answer[i][k] += arr1[i][j] * arr2[j][k]
                
    return answer