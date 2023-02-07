from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = i = 0
        d = {}
        for j, fruit in enumerate(fruits):
            d[fruit] = d.get(fruit, 0) + 1
            while len(d) > 2:
                d[fruits[i]] -= 1
                if d[fruits[i]] == 0: del d[fruits[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans