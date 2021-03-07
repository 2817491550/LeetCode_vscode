#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:
            return False
        if s[0] in {'+','-'}:
            sign=1
        else:
            sign=0
        e=s.find("e")
        if e==-1:
            e=s.find('E')
            if e==-1:
                sign_e=0
            else:
                sign_e=1
        else:
            sign_e=1
        print(e,123)
        if sign_e:
            if e==len(s)-1:
                return False 
            return self.isInt(s[e+1:]) and (self.isFloat(s[sign:e]) or self.isInt(s[sign:e])) 
        return self.isInt(s[sign:]) or self.isFloat(s[sign:])



        

        
    def isInt(self,s):
        if not s:
            return False
        if s[0] in {'+','-'}:
            sign=1
        else:
            sign=0
        if s[sign:]=='':
            return False
        for i in range(sign,len(s)):
            if 'a'<=s[i]<='z' or 'A'<=s[i]<='Z' or s[i]=='.' or s[i] in {'+','-'}:
                return False
        return True
        
            
    def isFloat(self,s):
        if s=='.':
            return False

        if not s:
            return False
        # if s[0] in {'+','-'}:
        #     sign=1
        # else:
        #     sign=0
        items={'1','2','3','4','5','6','7','8','9','0','.'}
        for c in s:
            if c not in items:
                # print(c)
                return False
            if c=='.':
                items.remove('.')
        return True

# @lc code=end

