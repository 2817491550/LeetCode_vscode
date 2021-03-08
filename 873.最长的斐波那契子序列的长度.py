#
# @lc app=leetcode.cn id=873 lang=python3
#
# [873] 最长的斐波那契子序列的长度
#

# @lc code=start
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        if not arr:
            return 0
        value_index_dict=dict()
        ans=0
        n=len(arr)
        dp=[[0]*n for _ in range(n)]
        
        for i in range(n):
            for j in range(i+1,n):
                dp[i][j]=2
        for i in range(n):
            for j in range(i+1,n):
                k=arr[j]-arr[i]
                if k in value_index_dict:
                    
                    dp[i][j]=max(dp[i][j],dp[value_index_dict[k]][i]+1)
                ans=max(dp[i][j],ans)
            value_index_dict[arr[i]]=i
        
        return ans if ans>2 else 0
        

# @lc code=end

