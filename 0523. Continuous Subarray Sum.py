class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1: return False
        sums, N = [nums[0]], len(nums)
        for num in nums[1:N]:
            temp = num + sums[-1]
            if temp % k == 0: return True
            sums.append(temp)
        subs = set()
        rem = sums[0] % k
        for idx in range(1, N):
            new = sums[idx] % k
            if new in subs: return True
            subs.add(rem)
            rem = new
        return False