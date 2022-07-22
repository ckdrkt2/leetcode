# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        greater, less = ListNode(), ListNode()
        g_cur, l_cur, cur = greater, less, head
        
        while cur:
            if cur.val >= x:
                g_cur.next = cur
                g_cur = g_cur.next
            else:
                l_cur.next = cur
                l_cur = l_cur.next
            cur = cur.next
              
        g_cur.next = None
        l_cur.next = greater.next
        return less.next
