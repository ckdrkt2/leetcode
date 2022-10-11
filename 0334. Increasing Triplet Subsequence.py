class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = 2147483647
        for n in nums:
            if n <= a:
                a = n
            elif n <= b:
                b = n
            else:
                return True
        return False