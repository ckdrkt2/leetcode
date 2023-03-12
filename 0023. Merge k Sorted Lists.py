from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst = []
        for link in lists:
            head = link
            while head:
                lst.append(head.val)
                head = head.next
        ans = ListNode()
        head = ans
        for n in sorted(lst):
            head.next = ListNode(n)
            head = head.next
        return ans.next