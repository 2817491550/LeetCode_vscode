#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        block=[set(range(1,10)) for _ in range(9)]
        row=[set(range(1,10)) for _ in range(9)]
        col=[set(range(1,10)) for _ in range(9)]
        empty=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    val=int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i//3)*3+j//3].remove(val)
                else:
                    empty.append((i,j))
        def back_track(iter=0):
            if iter==len(empty):
                return True
            i,j=empty[iter]
            b=(i//3)*3+j//3
            # print(row[i]&col[j]&block[b])
            for val in row[i]&col[j]&block[b]:
                
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j]=str(val)
                if back_track(iter+1):
                    return True
                row[i].add(val)
                col[j].add(val)
                block[b].add(val)
            return False
        back_track()
Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
# @lc code=end

