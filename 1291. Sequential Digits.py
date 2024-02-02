class Solution:
    def sequentialDigits(self, low, high):
        ans = []

        for i in range(1, 10):
            num, next = i, i + 1

            while num <= high and next <= 9:
                num = num * 10 + next
                if low <= num <= high:
                    ans.append(num)
                next += 1

        return sorted(ans)
