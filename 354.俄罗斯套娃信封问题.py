#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda t:(t[0],-t[1]))
        n=len(envelopes)
        counts=[1]*n
        for i in range(n):
            for j in range(i):
                if  envelopes[i][1]>envelopes[j][1]:
                        counts[i]=max(counts[j]+1,counts[i])
        return max(counts)
        

# @lc code=end

