class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n, totalSum, leftSum = len(nums), sum(nums), 0
        res = [float('inf'), float('inf')]
        for i, v in enumerate(nums):
            leftSum += v
            d = abs((leftSum // (i + 1)) - ((totalSum - leftSum) // (n - i - 1) if n - i - 1 != 0 else 0))
            res = min(res, [d, i])
        return res[1]