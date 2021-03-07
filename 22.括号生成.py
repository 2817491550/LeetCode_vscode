#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start

    
class Solution:
    result=[]
    def generateParenthesis(self, n: int) -> List[str]:
        self.result=[]
        self._generate(0,0,n,"")
        return self.result
    @functools.lru_cache(20)
    def _generate(self,left,right,n,s):
        # terminator
        if left==right==n:
            self.result.append(s) 
        # process
        # drill_down
        if left<n:
            self._generate(left+1,right,n,s+'(')
        if left>right:
            self._generate(left,right+1,n,s+')')
    # reverse states


# @lc code=end

