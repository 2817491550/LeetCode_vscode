#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_areas=0
        j=len(height)-1
        i=0
        while i<j:
            if height[i]<height[j]:
                h=height[i]
                i+=1
            else:
                h=height[j]
                j-=1
            max_areas=max(max_areas,(j-i+1)*h)


        return max_areas
# @lc code=end

