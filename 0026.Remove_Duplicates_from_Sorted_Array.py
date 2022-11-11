class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = Counter(nums)
        counter = 0
        for i in c:
            nums[counter] = i
            counter += 1
        return len(c)