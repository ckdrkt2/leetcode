class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        a = set(range(2, n))
        for i in range(2, int(n**0.5)+1):
            if i in a:
                a -= set(range(i*2, n, i))
        a = sorted(list(a))
        return len(a)