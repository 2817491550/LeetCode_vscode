#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        res=0
        ans=0
        for num in A:
            res=num+max(0,res)
            ans=max(ans,res)
        if ans==0:
            return max(A)
        resMin=0
        ansMin=0
        for num in A:
            resMin=num+min(0,resMin)
            ansMin=min(ansMin,resMin)
        


        return max(ans,sum(A)-ansMin)

# @lc code=end

