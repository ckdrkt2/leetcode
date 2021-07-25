class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        m, M = min(strs), max(strs)
        
        for i in range(len(m)):
            if m[i] != M[i]:
                return m[:i]
        return m