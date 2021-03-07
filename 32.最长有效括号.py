#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        max_num=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                stack.pop(-1)
                if stack==[]:
                    stack.append(i)
                else:
                    max_num=max(max_num,i-stack[-1])
        return max_num

# @lc code=end

