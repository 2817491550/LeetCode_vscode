#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j=0
        for i in range(len(s)):
            if j<len(g) and s[i]>=g[j]:
                j+=1
                i+=1
            else:
                i+=1
        return j





# @lc code=end

