def solution(arr):
    stk = []
    arr_len = len(arr)
    i = 0
    while i < arr_len:
        if not stk or stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()            
    return stk