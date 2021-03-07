#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        i=0
        while i<n:
            cnt=0
            sum_of_cost=0
            sum_of_gas=0
            while cnt<n:
                j=(i+cnt)%n
                sum_of_cost+=cost[j]
                sum_of_gas+=gas[j]
                if sum_of_cost>sum_of_gas:
                    break
                cnt+=1
            if cnt==n:
                return i
            else:
                i+=cnt+1
        return -1

# @lc code=end

