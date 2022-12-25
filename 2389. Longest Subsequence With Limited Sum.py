from bisect import bisect_right
from itertools import accumulate
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        return [bisect_right(list(accumulate(sorted(nums))), q) for q in queries]