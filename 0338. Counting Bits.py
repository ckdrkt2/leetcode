class Solution:
    def countBits(self, n: int) -> List[int]:
        a = []
        for i in range(n+1):
            num = i; c = 0
            while num >= 1:
                c += num%2
                num = num//2
            a.append(c)
        return a