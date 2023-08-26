from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        ans, maxNum = 1, pairs[0][1]
        for i in range(1, len(pairs)):
            if pairs[i][0] > maxNum:
                ans += 1
                maxNum = pairs[i][1]
        return ans
