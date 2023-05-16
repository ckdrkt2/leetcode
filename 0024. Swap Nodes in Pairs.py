from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:          
        if head is None or head.next is None:
            return head
        node=head.next.next
        
        head, head.next=head.next, head
        head.next.next=self.swapPairs(node)
        return head

