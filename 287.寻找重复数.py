#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # hast_set=set()
        # for num in nums:
        #     if num in hast_set:
        #         return num
            # hast_set.add(num) # hash 方式
        # 快慢指针：
        fast=slow=0
        slow=nums[slow]
        fast=nums[nums[fast]]
        while fast!=slow:
            slow=nums[slow]
            fast=nums[nums[fast]]
        fast=0
        while fast!=slow:
            slow=nums[slow]
            fast=nums[fast]
        return slow

        
# @lc code=end

