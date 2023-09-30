from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, n3 = [], float('-inf')
        for num in nums[::-1]:
            if num < n3: return True
            while stack and stack[-1] < num:
                n3 = stack.pop()
            stack.append(num)
        return False
