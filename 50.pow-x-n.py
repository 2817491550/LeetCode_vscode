
#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def fastPow(self,x,n):
        if n==0:
            return 1.0
        subresult=self.fastPow(x,n//2)
        if n%2:
            return subresult*subresult*x
        else:
            return subresult*subresult
        
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=-n 
        return self.fastPow(x,n)       
# @lc code=end

