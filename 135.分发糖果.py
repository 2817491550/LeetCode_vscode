#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        left=[0]*n
        candy=0
        for i in range(n):
            if i>0 and ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
            else:
                left[i]=1
        right=1
        for j in range(n-1,-1,-1):
            if j<n-1 and ratings[j]>ratings[j+1]:
                right+=1
            else:
                right=1
            candy+=max(left[j],right)
        return candy

                

# @lc code=end

