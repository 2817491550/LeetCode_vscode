#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red,white,blue=0,0,0
        k=0
        for i in nums:
            if i==0:
                red+=1
            elif i==1:
                white+=1
            else:
                blue+=1
        colors=(red,white,blue)
        for i in range(len(colors)):
            for j in range(colors[i]):
                nums[k]=i
                k+=1

                
# @lc code=end

