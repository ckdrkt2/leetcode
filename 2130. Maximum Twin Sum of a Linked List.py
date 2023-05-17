from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, pre, slow = pre, slow, slow.next
        ans = 0
        while slow and pre:
            ans = max(ans, slow.val + pre.val)
            slow = slow.next
            pre = pre.next
        return ans
