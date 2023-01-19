class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = t = 0
        d = [1] + [0] * k
        for n in nums:
            t = (t + n) % k
            if d[t]: ans += d[t]
            d[t] += 1
        return ans