#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i][0]:s[i]单独解码 不能为0   【=dp[i-1][0]+dp[i-1][1]
        # dp[i][1]:s[i-1]s[i]两位解码：1--26之间 【=dp[i-2][0]+dp[i-2][1]
        # 类似爬楼梯问题
        n=len(s)
        if not s:
            return 0
        if s[0]=='0':
            return 0
        dp=[[0,0] for _ in range(n)]
        if n==1:
            return 1
        dp[0][0]=1 if s[0]!='0' else 0
        dp[0][1]=0
        dp[1][0]=dp[0][0]+dp[0][1] if s[1]!='0' else 0
        dp[1][1]=1 if '1'<=s[0]+s[1]<='26' else 0
        for i in range(2,n):
            if s[i]=='0':
                dp[i][0]=0
            else:
                dp[i][0]=dp[i-1][0]+dp[i-1][1]
            if '1'<=s[i-1]+s[i]<='26':
                dp[i][1]=dp[i-2][0]+dp[i-2][1]
            else:
                dp[i][1]=0
        return dp[-1][0]+dp[-1][1]

# @lc code=end

