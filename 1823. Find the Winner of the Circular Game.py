"""
Josephus problem

원리는 제외하는 친구에 초첨을 두는 것이 아니라 승리하는 친구에 초첨을 두는 방식입니다.
n = 2일 때, 승리하는 친구의 index 값은 (0 + k)가 됩니다.
n = 3일 때, 승리하는 친구의 index 값은 (f(2) + k)가 됩니다.
이와 같은 식이 성립이 되기 때문에 결과적으로
n명일 때, 승리하는 친구의 index 값은 (f(n - 1) + k)가 되고, n명의 사람 밖에 없기 때문에 결과적으로,
(f(n - 1) + k) % n 이 됩니다.
"""

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + k) % i
        return ans + 1
