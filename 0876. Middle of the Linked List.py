# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, cnt = head, 0
        while head:
            cnt += 1
            head = head.next
        for _ in range(cnt // 2):
            cur = cur.next
        return cur