#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
# 

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        pairs={
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack=[]
        for item in s:
            if item in pairs:
                if not stack or pairs[item]!=stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(item)
        return len(stack)==0
# @lc code=end

