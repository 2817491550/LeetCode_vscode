#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        if len(s)<1 :
            return True
        s_ans=ord(s[0])
        for i in s[1:]:
            s_ans^=ord(i)
        for i in t:
            s_ans^=ord(i)
        return s_ans==0

        
        
            
        

# @lc code=end

