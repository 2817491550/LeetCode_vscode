#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=n-2
        j=n-1
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i>=0:
            while j>=0 and nums[j]<=nums[i]:
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
        l,r=i+1,n-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

# @lc code=end

