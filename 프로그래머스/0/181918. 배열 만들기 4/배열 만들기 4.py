def solution(arr):
    stk = []
    i = 0
    
    arr_size = len(arr)
    
    while i < arr_size:
        if not stk:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop()
    return stk