#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            char=strs[0][i]
            for j in range(1,len(strs)):
                if i==len(strs[j]) or strs[j][i]!=char:
                    return strs[0][:i]
        return strs[0]
                

# @lc code=end

