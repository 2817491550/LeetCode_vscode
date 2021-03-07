#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums, target: int) -> bool:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                return True
            if nums[l]==nums[mid] or nums[l]==nums[r]:
                l+=1
                continue
            if nums[r]==nums[mid]:
                r-=1
                continue
            if nums[mid]>nums[l]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<=target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return False

            

# @lc code=end

