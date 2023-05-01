from typing import List
class Solution:
    def average(self, salary: List[int]) -> float:
        m, M, mi, Mi = 1000000, 1000, 0, 0
        for i, n in enumerate(salary):
            if n < m: m, mi = n, i
            if n > M: M, Mi = n, i
        salary[mi], salary[Mi] = 0, 0
        return sum(salary) / (len(salary) - 2)