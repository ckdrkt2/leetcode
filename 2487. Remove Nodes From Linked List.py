class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        if not head.next: return head

        prev, cur = head, head.next
        while cur:
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp

        head.next, head = None, prev
        prev, cur = head, head.next

        while cur:
            if cur.val < prev.val:
                cur = cur.next
            else:
                tmp = cur.next
                cur.next = prev
                prev, cur = cur, tmp

        head.next, head = None, prev
        return head
