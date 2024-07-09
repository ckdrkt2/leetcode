from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waits, current = 0, 1

        for arrival, time in customers:
            if arrival <= current:
                current += time
            else:
                current = time + arrival
            waits += current - arrival

        return waits / len(customers)
