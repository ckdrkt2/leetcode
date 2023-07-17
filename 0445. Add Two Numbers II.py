from typing import Optional
from collections import deque
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        q1, q2 = deque(), deque()
        cur1, cur2 = l1, l2
        while cur1:
            q1.append(cur1)
            cur1 = cur1.next
        while cur2:
            q2.append(cur2)
            cur2 = cur2.next
        if len(q2) > len(q1):
            q1, q2, l1, l2 = q2, q1, l2, l1

        carry = 0
        for _ in range(len(q2)):
            node1, node2 = q1.pop(), q2.pop()
            s = node1.val + node2.val + carry
            node1.val, carry = s % 10, s // 10
        while carry and q1:
            node1 = q1.pop()
            s = node1.val + carry
            node1.val, carry = s % 10, s // 10
        if not q1 and carry:
            l1 = ListNode(carry, l1)

        return l1
