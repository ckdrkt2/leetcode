from typing import List
from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        ans = deque([''])
        d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        for digit in digits:
            for i in range(len(ans)):
                cur = ans.popleft()
                for c in d[digit]:
                    ans.append(cur + c)
        return ans
