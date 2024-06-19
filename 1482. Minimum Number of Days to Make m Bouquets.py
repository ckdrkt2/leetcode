from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1

        low, high, ans = min(bloomDay), max(bloomDay), 0
        while low <= high:
            mid = (low + high) // 2
            nums = cnt = 0
            for bloom in bloomDay:
                if mid >= bloom:
                    cnt += 1
                else:
                    nums += cnt // k
                    cnt = 0

            nums += cnt // k
            if nums >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
