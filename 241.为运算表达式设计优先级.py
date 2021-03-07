#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#

# @lc code=start
class Solution:
    def __init__(self):
        self.ops={'+','-','*'}
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        res=[]
        for i,char in enumerate(input):
            if char in self.ops:
                left=self.diffWaysToCompute(input[:i])
                right=self.diffWaysToCompute(input[i+1:])

                for l in left:
                    for r in right:
                        if char=='+':
                            res.append(l+r)
                        elif char=='-':
                            res.append(l-r)
                        else:
                            res.append(l*r)
        return res
        
# @lc code=end

