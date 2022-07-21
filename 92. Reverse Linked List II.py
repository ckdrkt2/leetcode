# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur, stack = head, []
        for i in range(right):
            if left - 1 <= i <= right - 1: stack.append(cur)
            cur = cur.next

        i, j = 0, len(stack) - 1

        while i < j:
            stack[i].val, stack[j].val = stack[j].val, stack[i].val
            i += 1
            j -= 1

        return head