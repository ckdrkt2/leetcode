from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ex = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1: ex = 0
            obstacleGrid[i][0] = ex
        ex = 1
        for j in range(1,n):
            if obstacleGrid[0][j] == 1: ex = 0
            obstacleGrid[0][j] = ex
        for i in range(1,m):
            for j in range(1,n):
                obstacleGrid[i][j] = 0 if obstacleGrid[i][j] else obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]
