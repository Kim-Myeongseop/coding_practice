def solution(arr):
    min_num = arr[0]
    min_idx = 0
    for idx in range(len(arr)):
        if arr[idx] < min_num:
            min_num = arr[idx]
            min_idx = idx
    del arr[min_idx]
    return arr if arr else [-1]