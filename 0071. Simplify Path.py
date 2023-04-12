class Solution:
    def simplifyPath(self, path: str) -> str:
        ans, i = path.split('/'), 0
        while i < len(ans):
            if ans[i] == '' or ans[i] == '.':
                ans.pop(i)
                continue
            if ans[i] == '..':
                ans.pop(i)
                if i > 0:
                    ans.pop(i-1)
                    i -= 1
                continue
            i += 1
        return '/' + '/'.join(ans)
