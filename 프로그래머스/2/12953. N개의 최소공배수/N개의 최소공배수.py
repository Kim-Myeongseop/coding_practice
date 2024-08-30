def solution(arr):
    def lcm(a, b):
        multi = a*b
        if a < b:
            a, b = b, a
        while b:
            a, b = b, a%b
        return multi//a
    
    total_lcm = 1
    for i in range(len(arr)):
        total_lcm = lcm(total_lcm, arr[i])
    return total_lcm