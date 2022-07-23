from bisect import bisect_left

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        lst = [nums.pop()]
        ans = [0]
        for n in nums[::-1]:
            c = bisect_left(lst, n)
            ans.append(c)
            lst.insert(c, n)
        return ans[::-1]
