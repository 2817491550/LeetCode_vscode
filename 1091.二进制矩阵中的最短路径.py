#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # BFS
        q=[(0,0,2)]
        n=len(grid)
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        elif n<=2:
            return n
        for i,j,dis in q:
            for x,y in [(i,j+1),(i,j-1),(i+1,j),(i-1,j),(i+1,j+1),(i-1,j-1),(i+1,j-1),(i-1,j+1)]:
                if 0<=x<n and 0<=y<n and not grid[x][y]:
                    if x==n-1 and y==n-1:
                        return dis
                    q+=[(x,y,dis+1)]
                    grid[x][y]=1
        return -1


        
# @lc code=end

