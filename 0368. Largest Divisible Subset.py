class Solution:


    def largestDivisibleSubset(self, nums):
        ans = {-1: set()}
        for x in sorted(nums):
            ans[x] = max((ans[d] for d in ans if x % d == 0), key=len) | {x}
        return list(max(ans.values(), key=len))
