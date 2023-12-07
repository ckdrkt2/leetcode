class Solution:
    def largestOddNumber(self, num: str) -> str:
        return num[:max(num.rfind(i) for i in '13579') + 1]
