#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for char in s:
            if char==']':
                sub=""
                while stack[-1]!='[':
                    sub=stack.pop()+sub
                stack.pop()
                num=""
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                stack.append(sub*int(num))
            else:
                stack.append(char)
        ans=""
        while stack:
            ans=stack.pop()+ans
        return ans


# @lc code=end

