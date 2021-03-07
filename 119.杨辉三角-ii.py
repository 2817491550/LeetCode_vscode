#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex+=1
        ret=[0]*rowIndex
        ret[0]=1
        rowIndex-=1
        for i in range(rowIndex):
            ret[0]=ret[i+1]=1
            for j in range(i,0,-1):
                ret[j]+=ret[j-1]
                


        return ret
# @lc code=end

