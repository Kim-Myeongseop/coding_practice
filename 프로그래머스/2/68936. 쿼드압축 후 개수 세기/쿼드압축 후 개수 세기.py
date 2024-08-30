# import sys
# sys.setrecursionlimit(10**6)

# def solution(arr):
#     answer = [0, 0]
#     def devide_conquer(matrix):
#         nonlocal answer
#         m = len(matrix)
#         if m == 1:
#             return matrix[0][0]
#         a = devide_conquer(list(map(lambda x: x[:m//2], matrix[:m//2])))
#         b = devide_conquer(list(map(lambda x: x[:m//2], matrix[m//2:])))
#         c = devide_conquer(list(map(lambda x: x[m//2:], matrix[:m//2])))
#         d = devide_conquer(list(map(lambda x: x[m//2:], matrix[m//2:])))
#         if a == b == c == d:
#             return a
#         else:
#             for x in [a, b, c, d]:
#                 if x == 0:
#                     answer[0] += 1
#                 elif x == 1:
#                     answer[1] += 1
#     devide_conquer(arr)
#     if answer == [0, 0]:   # 모든 숫자가 전부 같아서 한 번도 추가를 안하는 것 방지
#         if arr[0][0] == 0:
#             answer = [1, 0]
#         else:
#             answer = [0, 1]
#     return answer

# 다른 풀이 1
def solution(arr):
    answer = [0, 0]
    
    def devide_conquer(size, r, c):   # box의 한 변의 크기, 좌측 상단 행, 렬
        if size == 1:
            answer[arr[r][c]] += 1
            return
        
        start = arr[r][c]
        
        for i in range(size):
            for j in range(size):
                if start != arr[r+i][c+j]:   # 시작 값이랑 다른 값이 있으면 분할
                    devide_conquer(size//2, r, c)   # 좌측 상단 sub box
                    devide_conquer(size//2, r + size//2, c)   # 좌측 하단 sub box
                    devide_conquer(size//2, r, c + size//2)   # 우측 상단 sub box
                    devide_conquer(size//2, r + size//2, c + size//2)   # 우측 하단 sub box
                    return
        answer[start] += 1   # 한 번도 다른 값을 못 만나면 전부 그 값이라는 뜻
    
    devide_conquer(len(arr), 0, 0)
    return answer