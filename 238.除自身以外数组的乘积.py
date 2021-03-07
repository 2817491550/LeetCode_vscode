#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1]*n
        ans[0]=1
        for i in range(1,n):
            ans[i]=nums[i-1]*ans[i-1]
        r=1
        for i in reversed(range(n)):
            ans[i]*=r
            r*=nums[i]
        return ans
# @lc code=end

