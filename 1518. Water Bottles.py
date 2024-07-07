class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0

        while numBottles >= numExchange:

            k = numBottles // numExchange

            ans += numExchange * k
            numBottles -= numExchange * k

            numBottles += k

        return ans + numBottles
