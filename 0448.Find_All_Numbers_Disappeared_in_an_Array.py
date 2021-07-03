class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = [1 for i in range(len(nums))];b = []
        for i in nums:
            a[i-1] = 0
        print(a)
        for i in range(len(a)):
            if a[i]:
                b.append(i+1)
        return b