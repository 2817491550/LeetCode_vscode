#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n<1:return []
        self.result=[]
        self.cols=set()
        self.pie=set()
        self.na=set()
        self.DFS(n,0,[])
        return self.generateResult(n)
    def DFS(self, n,row,cur_state):
        # terminator
        if row>=n:
            self.result.append(cur_state)
            return 
        # current level
        for col in range(n):
            if col in self.cols or row+col in self.pie or row-col in self.na:
                continue # gonna die,filter it
            # update flags
            self.cols.add(col)
            self.pie.add(row+col)
            self.na.add(row-col)
            self.DFS(n,row+1,cur_state+[col])
            # reverse state
            self.cols.remove(col)
            
            self.pie.remove(row+col)
            self.na.remove(row-col)



    def generateResult(self,n):
        board=[]
        for res in self.result:
            for i in res:
                board.append("."*i+"Q"+"."*(n-i-1))
        return [board[i:i+n] for i in range(0,len(board),n)]
    
# @lc code=end

