#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L,n=len(needle),len(haystack)
        if L==0:
            return 0
        for start in range(n-L+1):
            if L>0 and haystack[start]==needle[0]:
                if haystack[start:start+L]==needle:
                    return start
        return -1
# @lc code=end


