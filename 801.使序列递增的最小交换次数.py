#
# @lc app=leetcode.cn id=801 lang=python3
#
# [801] 使序列递增的最小交换次数
#

# @lc code=start
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        no_swap1=0
        swap1=1 
        for i in range(1,len(A)):
            no_swap2,swap2=float('inf'),float('inf')
            if A[i]>A[i-1] and B[i]>B[i-1]:
                no_swap2=min(no_swap1,no_swap2)
                swap2=min(swap1+1,swap2)
            if A[i]>B[i-1] and B[i]>A[i-1]:
                no_swap2=min(swap1,no_swap2)
                swap2=min(no_swap1+1,swap2)
            swap1,no_swap1=swap2,no_swap2
        return min(swap1,no_swap1)
            


        
# @lc code=end

