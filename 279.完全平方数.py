#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
import math
class Solution:
    def numSquares(self, n: int) -> int:

        coins=[i**2 for i in range(1,int(math.sqrt(n))+1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, n + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[n] 



# @lc code=end

