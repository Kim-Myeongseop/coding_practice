# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_lst = []
        l2_lst = []
        while l1:
            l1_lst.append(str(l1.val))
            l1 = l1.next
        l1_lst = int(''.join(l1_lst[::-1]))
        while l2:
            l2_lst.append(str(l2.val))
            l2 = l2.next
        l2_lst = int(''.join(l2_lst[::-1]))
        
        n = None
        for s in str(l1_lst + l2_lst):
            n = ListNode(val=int(s), next=n)
        return n
        
        