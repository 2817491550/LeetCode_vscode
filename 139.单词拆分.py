#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        wordDict=set(wordDict)
        dp=[False]*(n+1)
        if not s:
            return True
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j]=True
    
        return dp[-1]
# @lc code=end

