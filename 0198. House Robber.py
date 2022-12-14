class Solution:
    def rob(self, nums: List[int]) -> int:
        a = b = 0
        for n in nums:
            a, b = b, max(a + n, b)
        return b