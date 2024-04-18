class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        answer = 0
        height = len(grid)
        width = len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    cnt = 4
                    if i<height-1:
                        cnt -= grid[i+1][j] == 1
                    if i>0:
                        cnt -= grid[i-1][j] == 1
                    if j<width-1:
                        cnt -= grid[i][j+1] == 1
                    if j>0:
                        cnt -= grid[i][j-1] == 1
                    print(cnt)
                    answer += cnt
        return answer            