class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = None
        for i in range(nums.count(None)):
            nums.remove(None)
        return len(nums)