#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        self.ret=[]
        for i in range(len(s)-len(p)+1):
            if self.helper(s[i:len(p)+i],p):
                self.ret.append(i)
        return self.ret
    def helper(self,sub_s,p):
        dic_s={}
        dic_p={}
        for i in sub_s:
            dic_s[i]=0
        for i in sub_s:
            dic_s[i]+=1
        for i in p:
            dic_p[i]=0
        for i in p:
            dic_p[i]+=1
        return dic_p==dic_s
        
        
# @lc code=end

