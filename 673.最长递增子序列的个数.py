#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        length=[1]*n
        count=[1]*n 
        for i,num in enumerate(nums):
            for j in range(i):
                if nums[j]<nums[i]:
                    if length[i]<=length[j]:
                         length[i]=length[j]+1
                         count[i]=count[j]
                    elif length[i]==length[j]+1:
                        count[i]+=count[j]
        longst=max(length)

        return sum(count[i] for i in range(n) if length[i]==longst)


# @lc code=end

