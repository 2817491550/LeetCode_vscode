#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low,high=0,len(nums)-1
        while low<high:
            mid=int(low+(high-low)/2)
            if nums[0]<=nums[mid] and (target>nums[mid] or target<nums[0]):
                low=mid+1
            elif nums[0]>nums[mid] and target<nums[0] and target>nums[mid]:
                low=mid+1
            else:
                high=mid
            
                
        return low if low==high and nums[low]==target else -1
            






# @lc code=end

