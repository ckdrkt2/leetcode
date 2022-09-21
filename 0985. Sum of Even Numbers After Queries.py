class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans, total = [], sum([n for n in nums if n % 2 == 0])
        for v, i in queries:
            cur = nums[i]
            nums[i] += v
            if cur % 2:
                if nums[i] % 2 == 0: total += nums[i]
            else:
                if nums[i] % 2: total -= cur
                else: total += v
            ans.append(total)
        return ans