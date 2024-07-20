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

# 다른 풀이 1                
'''
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        col_sum = colSum
        row_sum = rowSum
        
        mat = [[0]*len(col_sum) for i in range(len(row_sum))]
        i = 0
        j = 0
        while i < len(row_sum) and j < len(col_sum):
            mat[i][j] = min(row_sum[i], col_sum[j])
            if row_sum[i] == col_sum[j]:
                i += 1
                j += 1
            elif row_sum[i] > col_sum[j]:
                row_sum[i] -= col_sum[j]
                j += 1
            else:
                col_sum[j] -= row_sum[i]
                i += 1

        return mat
'''
                
        