#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)==1 or numRows==1:
            return s
        row=["" for _ in range(min(len(s),numRows))]
        goingDown=False
        curRow=0
        for c in s:
            row[curRow]+=c
            if curRow == 0 or curRow==numRows-1:
                goingDown=~goingDown
            curRow+=1 if goingDown else -1
        ret=""
        for c in row:
            ret+=c
        return ret
        
# @lc code=end

