#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Max_mult=-65535
        imax,imin=1,1
        for i in range(len(nums)):
            if nums[i]<0:
                imax,imin=imin,imax
            imax=max(imax*nums[i],nums[i])
            imin=min(imin*nums[i],nums[i])

            Max_mult=max(imax,Max_mult)
        return Max_mult
            
# @lc code=end

