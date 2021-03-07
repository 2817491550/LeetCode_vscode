#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return 
        row_zero_index=set()
        col_zero_index=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row_zero_index.add(i)
                    col_zero_index.add(j)
        for row in row_zero_index:
            for j in range(len(matrix[0])):
                matrix[row][j]=0
        for i in range(len(matrix)):
            for col in col_zero_index:
                matrix[i][col]=0


# @lc code=end

