#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        left,top,right,bottom=0,0,len(matrix[0])-1,len(matrix)-1
        ret=[]
        while left<=right and top<=bottom:
            for col in range(left,right+1):
                ret.append(matrix[top][col])
            for row in range(top+1,bottom+1):
                ret.append(matrix[row][right])
            if left<right and top<bottom:
                for col in range(right-1,left,-1):
                    ret.append(matrix[bottom][col])
                for row in range(bottom,top,-1):
                    ret.append(matrix[row][left])
            left,top,right,bottom=left+1,top+1,right-1,bottom-1
        return ret






# @lc code=end

