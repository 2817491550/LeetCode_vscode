#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret=[]
        size=len(candidates)
        def trace_back(begin,_target,level_ans):
            if _target==0:
                ret.append(level_ans)
                return
            if _target<0:
                return
            for i in range(begin,size):
                if _target-candidates[i]<0:
                    break
                trace_back(i,_target-candidates[i],level_ans+[candidates[i]])
        trace_back(0,target,[])
        return ret
# @lc code=end

