#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        back,ret=31,0
        
        while n:
            ret+=(n&1)<<back
            n=n>>1
            back-=1
        return ret

        
# @lc code=end

