class Solution:
    def knightDialer(self, n: int) -> int:
        dial = [1] * 10
        for _ in range(n - 1):
            dial = [dial[4] + dial[6],
                    dial[6] + dial[8],
                    dial[7] + dial[9],
                    dial[4] + dial[8],
                    dial[0] + dial[3] + dial[9],
                    0,
                    dial[0] + dial[1] + dial[7],
                    dial[2] + dial[6],
                    dial[1] + dial[3],
                    dial[2] + dial[4]]
        return sum(dial) % 1000000007
