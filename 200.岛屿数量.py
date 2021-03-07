#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        # isLand=0
        # self.g=grid
        # for i in range(len(self.g)):
        #     for j in range(len(self.g[0])):
        #         if self.g[i][j]=="0":
        #             continue
        #         isLand+=self.sink(i,j)
        # return isLand
        if not grid or len(grid)==0:
            return 0
        ret=0
        row_num=len(grid)
        col_num=len(grid[0])
        queue=[]
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j]=='1':
                    ret+=1
                    queue.append((i,j))
                    grid[i][j]='0'
                    while queue:
                        cur=queue.pop(0)
                        x=cur[0]
                        y=cur[1]
                        for k in range(4):
                            xx=x+dx[k]
                            yy=y+dy[k]
                            if 0<=xx<row_num and 0<=yy<col_num :
                                if grid[xx][yy]=='1':
                                    grid[xx][yy]='0'
                                    queue.append((xx,yy))
        return ret


    
    def sink(self,i,j):
        if self.g[i][j]=="0":
            return 0
        self.g[i][j]="0"
        dx=[1,-1,0,0]
        dy=[0,0,-1,1]
        for k in range(len(dx)):
            x=i+dx[k]
            y=j+dy[k]
            if 0<=x<len(self.g) and 0<=y<len(self.g[0]):
                if self.g[x][y]=="0":continue
                self.sink(x,y)
        return 1            
        







# @lc code=end

