#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_equal(islower,_target)->int:
            l=0
            r=len(nums)-1
            ans=len(nums)
            while l<=r:
                mid=l+(r-l)//2
                if nums[mid]>=_target and islower or nums[mid]>_target:
                    r=mid-1
                    ans=mid
                else:
                    l=mid+1
            return ans
        a=find_equal(True,target)
        b=find_equal(False,target)-1
        if b<len(nums) and a<=b and nums[a]==target and nums[b]==target:
            return [a,b]
        else:
            return [-1,-1]


# @lc code=end

