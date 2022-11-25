class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        result, stack = [0] * len(arr), [0]
        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]: stack.pop()
            j = stack[-1]
            result[i] = result[j] + (i - j) * arr[i]
            stack.append(i)
        return sum(result) % 1000000007