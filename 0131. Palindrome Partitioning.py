class Solution:
    def partition(self, s: str):
        ans = []
        self.dfs(s, [], ans)
        return ans

    def dfs(self, s, path, ans):
        if not s:
            ans.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], ans)

    def isPal(self, s):
        return s == s[::-1]
