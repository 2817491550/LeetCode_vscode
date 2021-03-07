#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k=nums[0]
        for i in range(1,len(nums)):
            k^=nums[i]
        return k




# @lc code=end

