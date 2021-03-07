#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    @functools.lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        # print(s,p)
        if not p:
            return not s
        if not s:
            return p[0]=='*' and self.isMatch(s,p[1:])
        first_match=bool(s) and p[0] in {s[0],'?'}
        if p[0]=='*':
            return self.isMatch(s,p[1:]) or self.isMatch(s[1:],p)
        else:
            return first_match and self.isMatch(s[1:],p[1:])






# @lc code=end

