from collections import Counter
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        endsAt = Counter()
        for n in nums:
            if counts[n]:
                if endsAt[n - 1]:
                    endsAt[n - 1] -= 1
                    endsAt[n] += 1
                elif counts[n + 1] and counts[n + 2]:
                    endsAt[n + 2] += 1
                    counts[n + 1] -= 1
                    counts[n + 2] -= 1
                else: return False
                counts[n] -= 1
        return True