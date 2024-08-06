# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_node = ListNode()
        main_node = current_node
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                current_node.next = ListNode(list1.val)
                current_node = current_node.next
                list1 = list1.next
            else:
                current_node.next = ListNode(list2.val)
                current_node = current_node.next
                list2 = list2.next
        
        if list1 == None:
            current_node.next = list2
        else:
            current_node.next = list1
        
        return main_node.next
