#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre=curr=0
        for money in nums:
            dp=max(pre+money,curr)
            pre=curr
            curr=dp
            
        return curr

       
                

# @lc code=end

