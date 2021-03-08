#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        size=len(nums)
        if not size:
            return []
        subsets={
            -1:set()
        }
        # T=O(nlogn),S=O(logn)
        for num in sorted(nums):
            subsets[num]=max([subsets[k] for k in subsets if not num%k],key=len)|{num}
        return list(max(subsets.values(),key=len))

# @lc code=end

