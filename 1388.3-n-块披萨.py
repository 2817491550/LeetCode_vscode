#
# @lc app=leetcode.cn id=1388 lang=python3
#
# [1388] 3n 块披萨
#

# @lc code=start
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n=len(slices)
        if not slices:
            return 0
        if n==1:
            return slices[0]
        if n==2:
            return max(slices[0],slices[1])
        pick_num=n//3
        def pick_profit(start,end):
            if end==start:
                return slices[end]
            dp=[[0]*(pick_num+1) for _ in range(end-start+1)]
            dp[0][0]=0
            dp[0][1]=slices[start]
            dp[1][0]=0
            dp[1][1]=max(slices[start],slices[start+1])
            for i in range(2,end-start+1):
                for j in range(1,pick_num+1):
                    dp[i][j]=max(dp[i-1][j],dp[i-2][j-1]+slices[start+i])
            return dp[-1][-1]
        return max(pick_profit(0,n-2),pick_profit(1,n-1))
        

# @lc code=end

