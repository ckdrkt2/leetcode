class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = [i for i in range(1, 10)]
        for _ in range(n - 1):
            for __ in range(len(ans)):
                num = ans.pop(0)
                last = num % 10
                u, d = last + k, last - k
                if u < 10: ans.append(num * 10 + u)
                if k > 0 and d >= 0: ans.append(num * 10 + d)
        return ans