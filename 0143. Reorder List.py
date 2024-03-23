from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        cur, slow.next = slow.next, None
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        cur = head
        while prev:
            tmp1, tmp2 = cur.next, prev.next
            cur.next = prev
            cur.next.next = tmp1
            cur, prev = tmp1, tmp2
