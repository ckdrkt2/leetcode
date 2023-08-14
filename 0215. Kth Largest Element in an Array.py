from typing import List
from random import choice
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = choice(nums)
        l, m, r = [], [], []
        for n in nums:
            if n > pivot:
                l.append(n)
            elif n == pivot:
                m.append(n)
            else:
                r.append(n)
        if k <= len(l):
            return self.findKthLargest(l, k)
        elif k > len(l) + len(m):
            return self.findKthLargest(r, k - len(l) - len(m))
        else:
            return m[0]
