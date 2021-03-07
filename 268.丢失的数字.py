#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        hash_set=[-1]*(n+1)
        for num in nums:
            hash_set[num]=num
        for i in range(n):
            if hash_set[i]==-1:
                return i
        return n
        
# @lc code=end

