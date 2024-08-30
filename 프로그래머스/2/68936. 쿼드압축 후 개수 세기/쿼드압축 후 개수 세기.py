import sys
sys.setrecursionlimit(10**6)

def solution(arr):
    answer = [0, 0]
    def devide_conquer(matrix):
        nonlocal answer
        m = len(matrix)
        if m == 1:
            return matrix[0][0]
        a = devide_conquer(list(map(lambda x: x[:m//2], matrix[:m//2])))
        b = devide_conquer(list(map(lambda x: x[:m//2], matrix[m//2:])))
        c = devide_conquer(list(map(lambda x: x[m//2:], matrix[:m//2])))
        d = devide_conquer(list(map(lambda x: x[m//2:], matrix[m//2:])))
        if a == b == c == d:
            return a
        else:
            for x in [a, b, c, d]:
                if x == 0:
                    answer[0] += 1
                elif x == 1:
                    answer[1] += 1
    devide_conquer(arr)
    if answer == [0, 0]:   # 모든 숫자가 전부 같아서 한 번도 추가를 안하는 것 방지
        if arr[0][0] == 0:
            answer = [1, 0]
        else:
            answer = [0, 1]
    return answer