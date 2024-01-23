from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        unique, ans = [''], 0
        for i in range(len(arr)):
            for j in range(len(unique)):
                new = arr[i] + unique[j]
                if len(set(new)) == len(new):
                    unique.append(new)
                    ans = max(ans, len(new))
        return ans
