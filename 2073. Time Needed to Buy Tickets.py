from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i, ticket in enumerate(tickets):
            ans += min(ticket, tickets[k] - int(i > k))
        return ans
