from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        ans, i, j = 0, 0, -1
        while i - j <= len(people):
            if people[i] + people[j] <= limit: j -= 1
            i += 1
            ans += 1
        return ans
