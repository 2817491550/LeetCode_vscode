#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_profit(nums):
            prev,curr=0,0
            for num in nums:
                prev,curr=curr,max(prev+num,curr)
            return curr
        return max(rob_profit(nums[1:]),rob_profit(nums[:-1])) if len(nums)>1 else nums[0]
# @lc code=end

