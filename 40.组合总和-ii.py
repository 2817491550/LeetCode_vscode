#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret=[]
        
        size=len(candidates)
        def trace_back(begin,_target,level_ans):
            if _target==0:
                ret.append(level_ans)
                return
            for i in range(begin,size):
                if _target<candidates[i]:
                    break
                if i >begin and candidates[i]==candidates[i-1]:
                    continue
                trace_back(i+1,_target-candidates[i],level_ans+[candidates[i]])
                          
        trace_back(0,target,[])

        return ret



# @lc code=end

