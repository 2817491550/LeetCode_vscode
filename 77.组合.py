#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret=[]
       
        def helper(current_state,j,now=0):
            if now>=k or k<0:
                ret.append(current_state)
                return
            for i in range(j,n+1):
                helper(current_state+[i],i+1,now+1)
        helper([],1)
        return ret

# @lc code=end

