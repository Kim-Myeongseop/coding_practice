# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        i = 0   # directions 중 몇 번째
        r, c = 0, 0   # start
        while head != None:
            matrix[r][c] = head.val
            head = head.next

            direction = directions[i]
            if not (0 <= r + direction[0] < m and 0 <= c + direction[1] < n and matrix[r+direction[0]][c+direction[1]] == -1):   # 방향 전환 해야되면
                i += 1
                if i == 4:
                    i = 0
                direction = directions[i]   # 방향 전환
            r += direction[0]
            c += direction[1]
        return matrix   