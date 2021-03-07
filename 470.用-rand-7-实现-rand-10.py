#
# @lc app=leetcode.cn id=470 lang=python3
#
# [470] 用 Rand7() 实现 Rand10()
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """

        while 1:
            row=rand7()
            col=rand7()
            idx=col+(row-1)*7
            if idx>40:
                break
        return 1+(idx-1)%10
        
        
# @lc code=end

