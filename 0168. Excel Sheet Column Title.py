class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a = columnNumber; r = []
        while True:
            b = a % 26
            a = a // 26
            if b > 0:
                r.insert(0,chr(b+64))
            else:
                if a > 0:
                    r.insert(0,"Z"); a -= 1
            if a == 0:
                break
        return ''.join(r)