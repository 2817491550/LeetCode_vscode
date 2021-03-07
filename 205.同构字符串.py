#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        orign_new_dict={}
        new_orign_dict={}
        if len(s)!=len(t):
            return True
        for i in range(len(s)):
            if t[i] in new_orign_dict:
                if s[i]!=new_orign_dict[t[i]]:
                    return False
            else:
                new_orign_dict[t[i]]=s[i]
            if s[i] in orign_new_dict:
                if t[i]!=orign_new_dict[s[i]]:
                    return False
            else:
                orign_new_dict[s[i]]=t[i]
        return True
# @lc code=end

