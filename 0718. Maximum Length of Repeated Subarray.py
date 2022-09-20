class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        s2 = "".join([chr(x) for x in nums2])
        s1 = "".join([chr(x) for x in nums1])
        n, res, i = len(s1), 0, 0
        for j in range(1, n + 1):
            if s1[i:j] in s2:
                res = max(res, j - i)
            elif i < j:
                i += 1
        return res