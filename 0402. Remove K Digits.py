class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        a, n = '', 0
        while n < 10 and num and k:
            i = num.find(str(n))
            if i == -1 or i > k:
                n += 1
                continue
            if i <= k:
                num = num[i+1:]
                k -= i
                a += str(n) if n or (a and a[-1] != '0') else ''
                n = 0
        a += num
        num = a[:-k].lstrip('0') if k else a.lstrip('0')
        return num if num else '0'
