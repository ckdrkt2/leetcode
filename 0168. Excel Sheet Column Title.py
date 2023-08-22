class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a, ans = columnNumber, []
        while True:
            a, b = a // 26, a % 26
            if b > 0:
                ans.insert(0, chr(b + 64))
            else:
                if a > 0:
                    ans.insert(0, "Z")
                    a -= 1
            if a == 0: break
        return ''.join(ans)
