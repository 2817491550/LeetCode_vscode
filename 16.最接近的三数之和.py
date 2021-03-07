#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        i,j=0,2
        _sum=sum(nums[i:j+1])
        if _sum>=target:
            return _sum
        ans=_sum
        while i<=j and j<len(nums) and i>=0:
            if _sum<target:
                j+=1
                if j<len(nums):
                    _sum-=nums[i]
                    i+=1
                    _sum+=nums[j]
                    ans=_sum
                else:
                    break
            else:
                ans=_sum if _sum-target<target-ans else ans
                break
        return ans
            


            


# @lc code=end

