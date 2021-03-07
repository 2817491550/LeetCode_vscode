#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        hash_set=set()
        while i<n:
            if nums[i] in hash_set:
                del nums[i]
                n-=1
                i-=1
            hash_set.add(nums[i])
            i+=1
        return n

# @lc code=end

