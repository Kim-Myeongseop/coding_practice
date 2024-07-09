# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # 정렬하고 중간 값을 노드로 만들고 나머지 좌우 리스트의 중간 값을 좌우 값으로 하는 방식으로 구현(재귀)
        new_list = []

        # new_list에 숫자 정렬(left -> root -> right 순)
        def in_order(node):
            if not node:   # node가 없으면 None return
                return
            in_order(node.left)
            new_list.append(node.val)
            in_order(node.right)

        # node를 만드는 재귀 함수를 만들어 tree만들기
        def build(left, right):
            if left > right:
                return
            mid = (left+right) >> 1
            node = TreeNode(new_list[mid])
            node.left = build(left, mid-1)
            node.right = build(mid+1, right)
            return node    
        
        in_order(root)
        return build(0, len(new_list)-1)