class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not len(needle):
            return 0
        elif needle in haystack:
            return len(haystack.split(needle)[0])
        else:
            return -1