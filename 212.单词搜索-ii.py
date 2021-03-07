#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
import  collections
# @lc code=start
class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.dx=[-1,1,0,0]
        self.dy=[0,0,1,-1]
        self.end_sign='#'
        if not board or not board[0]:
            return []
        if not words :
            return []
        self.result=set()
        root=collections.defaultdict()
        for word in words:
            node=root
            for char in word:
                node=node.setdefault(char,collections.defaultdict())
            node[self.end_sign]=self.end_sign
        self.m,self.n=len(board),len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self._dfs(board,i,j,"",root)
        return list(self.result)
    
    def _dfs(self,board,i,j,curr_res,cur_dict):
        curr_res+=board[i][j]
        cur_dict=cur_dict[board[i][j]]
        if self.end_sign in cur_dict:      
            self.result.add(curr_res)
        tmp,board[i][j]=board[i][j],'@'
        for k in range(4):
            x,y = i+self.dx[k],j+self.dy[k]
            if 0<=x <self.m and 0<=y<self.n\
                and board[x][y]!='@' and board[x][y] in cur_dict:
                self._dfs(board,x,y,curr_res,cur_dict)
        board[i][j]=tmp
            

# @lc code=end

