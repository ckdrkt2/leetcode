class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, maxSum, curMax, minSum, curMin = 0, nums[0], 0, nums[0], 0
        for n in nums:
            curMax = max(curMax + n, n)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + n, n)
            minSum = min(minSum, curMin)
            total += n
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum