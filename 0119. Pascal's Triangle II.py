class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ex = []
        for i in range(rowIndex+1):
            now = []
            for j in range(i+1):
                if j == i or j == 0:
                    now.append(1)
                else:
                    now.append(ex[j-1] + ex[j])
            ex = [n for n in now]
        return now
        
        