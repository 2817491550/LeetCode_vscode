#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        step,end,boundary=0,0,0
        for i in range(n-1):
            if boundary>=i:
                boundary=max(boundary,i+nums[i])
                if i==end:
                    end=boundary
                    step+=1
        return step
# @lc code=end

