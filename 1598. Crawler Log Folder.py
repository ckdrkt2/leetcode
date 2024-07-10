from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log == "../":
                if ans == 0: continue
                ans -= 1
            elif log == "./":
                pass
            else:
                ans += 1
        return ans
