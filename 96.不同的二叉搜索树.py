#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        # G_function=[0]*(n+1)
        # G_function[0]=G_function[1]=1
        # for i in range(2,n+1):
        #     for j in range(1,i+1):
        #         G_function[i]+=G_function[j-1]*G_function[i-j]
        # return G_function[n]


        
        # 卡塔兰树
        c=1
        for i in range(n):
            c=2*c*(2*i+1)//(i+2)
        return c
# @lc code=end

