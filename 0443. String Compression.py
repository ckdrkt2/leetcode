from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n < 2: return n
        anchor = ans = 0
        for pos, char in enumerate(chars):
            if (pos + 1) == n or char != chars[pos+1]:
                chars[ans] = char
                ans += 1
                if pos > anchor:
                    repeated_times = pos - anchor + 1
                    for num in str(repeated_times):
                        chars[ans] = num
                        ans += 1
                anchor = pos + 1
        return ans