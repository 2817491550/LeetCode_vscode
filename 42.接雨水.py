#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max,right_max=0,0
        n=len(height)
        left,right=0,n-1
        ans=0
        while left<right:
            if height[left]<height[right]:
                left_max=height[left] if height[left]>left_max else left_max
                ans+=left_max-height[left]
                left+=1
            else:
                right_max=height[right] if height[right]>right_max else right_max
                ans+=right_max-height[right]
                right-=1
        return ans
# @lc code=end

