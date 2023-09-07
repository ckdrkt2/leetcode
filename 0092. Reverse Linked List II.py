from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ans = ListNode(0)
        ans.next = head

        pre = ans
        cur = ans.next

        for i in range(1, left):
            cur = cur.next
            pre = pre.next

        for i in range(right - left):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp

        return ans.next
