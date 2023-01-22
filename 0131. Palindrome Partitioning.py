class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans, path, l = [], [], len(s)
        def dfs(i):
            if i == l:
                ans.append(path.copy())
                return
            for j in range(i, l):
                st = s[i: j+1]
                if st == st[::-1]:
                    path.append(st)
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return ans