#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
from collections import  deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        n,m=len(board),len(board[0])
        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m or board[i][j]!='O':
                return 
            board[i][j]='A'
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        for i in range(n):
            dfs(i,0)
            dfs(i,m-1)
        for j in range(1,m-1):
            dfs(0,j)
            dfs(n-1,j)
        for i in range(n):
            for j in range(m):
                if board[i][j]=='A':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
        
        

# @lc code=end

