class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return sum(c.lower() in 'aeiou' for c in s[:len(s)//2]) == sum(c.lower() in 'aeiou' for c in s[len(s)//2:])