from collections import Counter
class Solution:
    def sortVowels(self, s: str) -> str:
        chars = Counter(s)
        vowels = []
        for char in chars.keys():
            if char in "AEIOUaeiou":
                vowels.append(char)
                s = s.replace(char, '_')
        vowels.sort()
        for char in vowels:
            s = s.replace('_', char, chars[char])
        return s
