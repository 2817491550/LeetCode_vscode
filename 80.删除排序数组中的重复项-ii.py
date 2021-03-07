#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums) -> int:
        n=len(nums)
        if not nums:
            return 0
        i=2
        while i<n:
            if nums[i]==nums[i-1]==nums[i-2]:
                del nums[i]
                n-=1
                i-=1
            i+=1
        return len(nums)




# @lc code=end

