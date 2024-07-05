from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        first = prev = -1
        m_dist, idx = 100000, 0
        while cur.next.next:
            if cur.val > cur.next.val < cur.next.next.val or cur.val < cur.next.val > cur.next.next.val:
                if prev == -1:
                    first = prev = idx
                else:
                    m_dist = min(m_dist, idx - prev)
                    prev = idx
            cur = cur.next
            idx += 1

        if first == -1 or first == prev: return [-1, -1]
        return [m_dist, prev - first]
