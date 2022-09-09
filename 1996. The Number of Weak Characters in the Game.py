class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0],x[1]))
        ans, m = 0, 0
        for _, d in properties:
            if d < m: ans += 1
            else: m = d
        return ans