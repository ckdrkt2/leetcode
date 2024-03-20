class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = ListNode(next=list1)
        for _ in range(a): head = head.next
        head_a = head
        for _ in range(b - a + 1): head = head.next
        head_b = head.next
        head_a.next = list2
        while list2.next: list2 = list2.next
        list2.next = head_b
        return list1
