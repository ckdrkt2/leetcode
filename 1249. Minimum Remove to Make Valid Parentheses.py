class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sList, ans = list(s), []
        for i, c in enumerate(sList):
            if c =='(':
                ans.append(i)
            elif c == ')':
                if ans:
                    ans.pop()
                else:
                    sList[i] = ''
        while ans:
            sList[ans.pop()] = ''

        return ''.join(sList)
