#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除与获得点数
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n=len(nums)
        add_l=[0]*(max(nums)+1)
        for num in nums:
            add_l[num]+=1
        def rob_profit(nums):
            prev,curr=0,0
            for i,num in enumerate(nums):
                prev,curr=curr,max(curr,prev+num*i)
            return curr
        return rob_profit(add_l) 
# @lc code=end

