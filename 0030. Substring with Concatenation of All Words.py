from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans, lenword = [], len(words[0])
        l = len(words) * lenword
        for i in range(len(s) - l + 1):
            seen = Counter(words)
            seen_words = 0
            for j in range(i, i + l, lenword):
                sub_str = s[j : j + lenword]
                if sub_str in seen and seen[sub_str] > 0:
                    seen[sub_str] -= 1
                    seen_words += 1
                else: break
            if(seen_words == len(words)): ans.append(i)
        return ans