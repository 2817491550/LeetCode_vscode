#
# @lc app=leetcode.cn id=1027 lang=python3
#
# [1027] 最长等差数列
#

# @lc code=start
class Solution:
    def longestArithSeqLength(self, A) -> int:
    
        value_index_dict=dict()
        n=len(A)
        dp=[[2 for _ in range(n)] for _ in range(n)]
        
        ans=2
        for i in range(n):
            for j in range(i+1,n):
                A_k=2*A[i]-A[j]
                if A_k in value_index_dict:
                    dp[i][j]=max(dp[i][j],dp[value_index_dict[A_k]][i]+1)
                ans=max(ans,dp[i][j])
            value_index_dict[A[i]]=i
        
        return ans 

# @lc code=end

