#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    @functools.lru_cache(100)
    def climbStairs(self, n: int) -> int:
        g=0
        f=1
        for i in range(n):
            t=f
            f+=g
            g=t
        return f
# @lc code=end

