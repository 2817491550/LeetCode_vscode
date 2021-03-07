#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        if obstacleGrid[0][0]==1:
            return 0
       
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        
        dp=[[0]*n for _ in range(m)]
       
        for i in range(m):
            for j in range(n):
                if not obstacleGrid[i][j]:
                    if i==j==0:
                        dp[i][j]=1
                    else:
                        a=dp[i-1][j] if i!=0 else 0
                        b=dp[i][j-1] if j!=0 else 0
                        dp[i][j]=a+b

        return dp[-1][-1]

# @lc code=end

