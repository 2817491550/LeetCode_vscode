#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=list()
        n=len(nums)
        ret=[-1]*n 
        for i in range(2*n-1):
            while stack and nums[stack[-1]]<nums[i%n]:
                ret[stack.pop()]=nums[i%n]
            stack.append(i%n)
        return ret


        
# @lc code=end

