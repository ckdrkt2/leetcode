# Time Limit Exceeded
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n < 3:
#             return n
#         return self.climbStairs(n-1) + self.climbStairs(n-2)
class Solution:
    def climbStairs(self, n: int) -> int:
        a = [1,2]
        for i in range(3,n+1):
            a.append(a[i-2]+a[i-3])
        return a[n-1]