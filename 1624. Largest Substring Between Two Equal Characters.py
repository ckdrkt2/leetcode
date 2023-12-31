class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans, d = -1, {}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
            else:
                ans = max(ans, i - d[c] - 1)
        return ans
