from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = head
        while front.next:
            cur = front.next
            while cur.val != 0:
                front.val += cur.val
                front.next = cur.next
                cur = cur.next
            if front.next.next is None:
                front.next = None
            front = cur
        return head
