#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        r=[]
        for s in path.split('/'):
            r={
                '':r,
                '.':r,
                '..':r[:-1]         
            }.get(s,r+[s])
        return '/'+'/'.join(r)
# @lc code=end

