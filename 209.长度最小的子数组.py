#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        min_=len(nums)
        if not nums:
            return 0
        if len(nums)==1:
            if nums[0]>=target:
                return 1
            else:
                return 0

        i,j=0,0
        if sum(nums)<target:
            return 0
        sum_=nums[0]
        # print(sum_)
        while i<=j and j<len(nums) and i<len(nums):
            if sum_>=target:
                sum_-=nums[i]
                min_=min(min_,j-i+1)
                i+=1
            else:
                j+=1
                if j<len(nums):
                    sum_+=nums[j]
            # print(sum_)
        # print(min_)

            
        return max(0,min_)
# @lc code=end
print(
Solution().minSubArrayLen(7,[2,3,1,2,4,3])
)