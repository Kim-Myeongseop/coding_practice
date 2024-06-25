def solution(n, lost, reserve):
    answer = min(n - len(lost) + len(reserve), n)
    answer = 0
    arr = [1 for _ in range(n)]
    for l in lost:
        arr[l-1] -= 1
    for r in reserve:
        arr[r-1] += 1
    
    for i in range(n):
        if i == 0 and arr[i] == 2 and arr[i+1] == 0:
            arr[i] = 1
            arr[i+1] = 1
        if i == n-1 and arr[i] == 2 and arr[i-1] == 0:
            arr[i] = 1
            arr[i-1] = 1
        if i > 0 and i < n-1 and arr[i] == 2:
            if arr[i-1] == 0:
                arr[i-1] = 1
                arr[i] = 1
            elif arr[i+1] == 0:
                arr[i+1] = 1
                arr[i] = 1          
    
    for a in arr:
        if a != 0:
            answer += 1
    return answer