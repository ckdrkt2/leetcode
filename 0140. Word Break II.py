from typing import List
from collections import defaultdict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        strs = defaultdict(list)
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                beg = i - len(word) + 1
                if beg >= 0 and (beg == 0 or dp[beg - 1]) and word == s[beg:i + 1]:
                    dp[i] = True
                    if beg == 0:
                        strs[i].append(word)
                    else:
                        for sentence in strs[beg - 1]:
                            strs[i].append(sentence + ' ' + word)
        return strs[len(s) - 1]
