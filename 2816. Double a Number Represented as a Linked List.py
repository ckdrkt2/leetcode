from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = cur = ListNode()

        while head:
            double = 2 * head.val
            if double > 9:
                cur.val += 1
            cur.next = ListNode(val = double % 10)
            cur, head = cur.next, head.next

        return ans if ans.val else ans.next
