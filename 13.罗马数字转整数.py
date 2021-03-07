#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_symbol={
            "I":1,
            "V":5,
            "X":10,
            "C":100,
            "L":50,
            "D":500,
            "M":1000
        }
        pre_num=s[0]
        ans=0
        for i in range(1,len(s)):
            if roman_symbol[pre_num]>=roman_symbol[s[i]]:
                ans+=roman_symbol[pre_num]
            else:
                ans-=roman_symbol[pre_num]
            pre_num=s[i]
        ans+=roman_symbol[pre_num]
        return ans

# @lc code=end

