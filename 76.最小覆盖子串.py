#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        T_alphaBet={c:0 for c in s}
        for c in s:
            T_alphaBet[c]+=1
        

# @lc code=end

