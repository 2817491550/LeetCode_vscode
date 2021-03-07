#
# @lc app=leetcode.cn id=915 lang=python3
#
# [915] 分割数组
#

# @lc code=start
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        n=len(A)
        left_max=[0]*(n+1)
        right_min=[0]*(n+1)
        left_max[1]=A[0]
        for i in range(1,n):
            left_max[i+1]=max(left_max[i], A[i])
        right_min[n]=A[-1]
        for i in range(n-1,-1,-1):
            right_min[i]=min(A[i],right_min[i+1])
        for i in range(1,n+1):
            if left_max[i]<=right_min[i]:
                return i
        
        
# @lc code=end

