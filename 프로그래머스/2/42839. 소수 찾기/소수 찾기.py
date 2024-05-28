def permutation(arr, r=None):
    if r == None:
        r = len(arr)
        
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for new_arr in permutation(arr[:i]+arr[i+1:], r-1):
                yield [arr[i]] + new_arr

def isprime(num):
    sign = True
    sqrt = round(num**(1/2))
    for n in range(2, sqrt+1):
        if num/n == int(num/n):
            sign = False
    return sign if num != 1 else False

def solution(numbers):
    answer = 0
    numbers = [number for number in numbers]
    num_list = []
    
    for i in range(1, len(numbers)+1):
        fn = permutation(numbers, i)
        for item in fn:
            num_list.append(''.join(item))
    
    num_list = list(set(num_list))
    
    for num in num_list:
        if num == '2':
            answer += 1
        elif num[0] == '0' or num[-1] in ['0','2','4','6','8']:   # 검사 불필요
            continue
        else:
            if isprime(int(num)):
                answer += 1
    return answer