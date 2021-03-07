#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        
        for k in range(len(nums)-2):
            if k>0 and nums[k]==nums[k-1]:
                continue
            i=k+1
            j=len(nums)-1
            while i<j:
                Sum=nums[i]+nums[j]+nums[k]
                if Sum<0:
                    i+=1
                elif Sum>0:
                    j-=1
                else:
                    result.append([nums[k],nums[i],nums[j]])
                    while i<j and nums[i+1]==nums[i]:
                        i+=1
                    while i<j and nums[j-1]==nums[j]:
                        j-=1
                    i+=1
                    j-=1
           
        return result


# @lc code=end

