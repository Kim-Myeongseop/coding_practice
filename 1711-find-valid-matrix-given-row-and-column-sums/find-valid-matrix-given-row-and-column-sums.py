class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        matrix = [[0]*n for _ in range(m)]   # m x n matrix
        for row in range(m):
            for col in range(n):
                if colSum[col] > 0 and rowSum[row] > 0:
                    value = min(colSum[col], rowSum[row])
                    matrix[row][col] = value
                    colSum[col] -= value
                    rowSum[row] -= value
        return matrix
                
                
                
        