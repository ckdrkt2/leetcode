# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# recursive solution
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        if head.val == val:
            return self.removeElements(head.next, val)
        
        nextElement = self.removeElements(head.next, val)
        head.next = nextElement
        return head