#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # stack=[-1]
        # max_num=0
        # for i in range(len(s)):
        #     if s[i]=='(':
        #         stack.append(i)
        #     elif s[i]==')':
        #         stack.pop(-1)
        #         if stack==[]:
        #             stack.append(i)
        #         else:
        #             max_num=max(max_num,i-stack[-1])
        # return max_num
        # ^ 栈方法
        # down below:
        # dynamic programming
        size=len(s)
        dp=[0]*size
        max_valid_num=0
        for i in range(1,size):
            if s[i]=='(':
                dp[i]=0
                continue
            if s[i]==')':
                if s[i-1]=='(':
                    if i>=2:
                        dp[i]+=dp[i-2]+2
                    else:
                        dp[i]=2
                elif s[i-1]==')':
                    if (i-dp[i-1]-1)>=0 and s[i-dp[i-1]-1]=='(':
                        dp[i]=dp[i-1]+2
                        if i-dp[i-1]-2>=0:
                            dp[i]+=dp[i-dp[i-1]-2]
            max_valid_num=max(max_valid_num,dp[i])
        return max_valid_num



# @lc code=end

