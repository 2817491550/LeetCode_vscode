#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#

# @lc code=start
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        rest_char=Counter(s)
        
        seen=set()
        stack=[]
        for c in s:
            
            if c not in seen:
                while stack and stack[-1]>c and rest_char[stack[-1]]>0:
                    seen.remove(stack.pop())
                stack.append(c)
                seen.add(c)
            rest_char[c]-=1
            # print(stack)
        
        return "".join(stack)



# @lc code=end

