#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max_k=2
        dp_i20,dp_i10=0,0
        dp_i21,dp_i11=-float("inf"),-float("inf")
        for price in prices:
            dp_i20=max(dp_i20,dp_i21+price)
            dp_i21=max(dp_i21,dp_i10-price)
            dp_i10=max(dp_i10,dp_i11+price)
            dp_i11=max(-price,dp_i11)
        return dp_i20




# @lc code=end

