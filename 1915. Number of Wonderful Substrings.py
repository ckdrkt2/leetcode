class Solution(object):
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024
        count[0] = 1
        bit = ans = 0

        for c in word:
            idx = ord(c) - ord('a')
            bit ^= 1 << idx
            ans += count[bit]
            for i in range(10):
                ans += count[bit ^ (1 << i)]
            count[bit] += 1

        return ans
