from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magdict, randict = Counter(magazine), Counter(ransomNote)
        for k in randict:
            if randict[k] > magdict[k]: return False
        return True
