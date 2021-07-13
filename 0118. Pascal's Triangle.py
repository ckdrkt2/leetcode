class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ex = [1]; out = []; now = []
        for i in range(numRows):
            for j in range(i+1):
                if j == i or j == 0:
                    now.append(1)
                else:
                    now.append(ex[j-1] + ex[j])
            out.append(now)
            ex = [n for n in now]
            now = []
        return out