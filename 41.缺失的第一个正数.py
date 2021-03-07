#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        exist_nums={nums[i] for i in range(n)}
        for i in range(1,65536):
            if i not in exist_nums:
                return i
            
# @lc code=end

