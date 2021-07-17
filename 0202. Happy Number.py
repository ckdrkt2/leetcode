class Solution:
    def isHappy(self, n: int) -> bool:
        t = []
        while True:
            a = 0
            for i in str(n):
                a += (int(i))**2
            if a == 1:
                return True
            if a not in t:
                t.append(a)
            else:
                return False
            n = a
            print(n)