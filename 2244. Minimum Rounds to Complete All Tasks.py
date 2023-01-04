from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ans, d = 0, Counter(tasks)
        for n in d:
            if d[n] == 1: return -1
            ans += d[n] // 3
            if d[n] % 3 > 0: ans += 1
        return ans