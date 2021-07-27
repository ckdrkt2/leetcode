# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        a = None
        
        while head:
            b = ListNode()
            b.val = head.val
            b.next = a
            a = b
            head = head.next
        return a
            