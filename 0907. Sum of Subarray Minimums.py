from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        ans, stack = [0] * len(arr), [0]
        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]: stack.pop()
            j = stack[-1]
            ans[i] = ans[j] + (i - j) * arr[i]
            stack.append(i)
        return sum(ans) % 1000000007
