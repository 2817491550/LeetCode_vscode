#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:  
        m=len(text1)
        n=len(text2)
        LCS_List=[[0]*(n+1) for _ in range(m+1)]
        if not text1 or not text2:
            return 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]!=text2[j-1]:
                    LCS_List[i][j]=max(LCS_List[i-1][j],LCS_List[i][j-1])
                else:
                    LCS_List[i][j]=LCS_List[i-1][j-1]+1
        return LCS_List[-1][-1]

        











# @lc code=end

