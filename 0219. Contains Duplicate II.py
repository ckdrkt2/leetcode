class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, n in enumerate(nums):
            if i - d.get(n, -100000) <= k: return True
            d[n] = i
        return False