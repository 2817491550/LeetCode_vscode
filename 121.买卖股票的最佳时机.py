#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp_i_0=0
        dp_i_1=-prices[0]
        for i in range(1,n):
            dp_i_0=max(dp_i_0,dp_i_1+prices[i])
            dp_i_1=max(-prices[i],dp_i_1)
        return dp_i_0

            

# @lc code=end

