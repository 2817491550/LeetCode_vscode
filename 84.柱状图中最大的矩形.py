#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        left,right=[0]*n,[0]*n
        stack=[]
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                 stack.pop(-1)
            left[i]=stack[-1] if stack else -1
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                 stack.pop(-1)
            right[i]=stack[-1] if stack else n
            stack.append(i)
        area=[0]*n 
        for i in range(n):
            area[i]=heights[i]*(right[i]-left[i]-1)
        return max(area)



        
        
 #@lc code=end

 