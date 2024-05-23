import sys
sys.setrecursionlimit(10**8)
#input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]

def divide(array):
    n = len(array)
    if n == 1:
        return array[0][0]
    else:
        lu = [row[:n//2] for row in array[:n//2]]
        ru = [row[n//2:] for row in array[:n//2]]
        ld = [row[:n//2] for row in array[n//2:]]
        rd = [row[n//2:] for row in array[n//2:]]
        answer = [divide(lu), divide(ru), divide(ld), divide(rd)]
        if answer == [0,0,0,0]:
            return 0
        elif answer == [1,1,1,1]:
            return 1
        else:
            return answer
        
output = divide(arr)
output = str(output).replace('[', '(').replace(']', ')').replace(',', '').replace(' ', '')
print(output)