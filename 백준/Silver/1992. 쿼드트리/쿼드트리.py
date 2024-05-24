import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

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



def conquer(x, y, n):
    check = arr[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != check:
                print('(', end='')
                conquer(x, y, n//2)
                conquer(x, y+n//2, n//2)
                conquer(x+n//2, y, n//2)
                conquer(x+n//2, y+n//2, n//2)
                print(')', end='')
                return
    print(check, end='')

# conquer(0, 0, N)
    
