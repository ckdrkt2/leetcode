class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # O(n^2)
        # a = []
        # for i in nums:
        #     if i not in a:
        #         a.append(i)
        #     else:
        #         a.remove(i)
        # return a.pop()
        return 2*sum(set(nums)) - sum(nums)