#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        is_partition=[[True]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                is_partition[i][j]=(is_partition[i+1][j-1]) and (s[i]==s[j])
        dp=[float('inf')]*n
        for i in range(n):
            if is_partition[0][i]:
                dp[i]=0
            else:
                for j in range(i):
                    if is_partition[j+1][i]:
                        dp[i]=min(dp[i],dp[j]+1)
        return dp[-1]





# @lc code=end

