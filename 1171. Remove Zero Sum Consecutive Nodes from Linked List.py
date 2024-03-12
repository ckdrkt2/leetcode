from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        mapping, prefix_sum = {}, 0
        while cur != None:
            prefix_sum += cur.val
            if prefix_sum in mapping:
                node = mapping[prefix_sum]
                temp = mapping[prefix_sum].next
                temp_sum = prefix_sum
                while temp != cur:
                    temp_sum += temp.val
                    del mapping[temp_sum]
                    temp = temp.next

                node.next = cur.next
                cur = cur.next
            else:
                mapping[prefix_sum] = cur
                cur = cur.next

        return dummy.next
