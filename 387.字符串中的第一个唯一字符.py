#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        od=OrderedDict()
        for i in range(len(s)):
            od[s[i]]=[0,i]
        for i in s:
            od[i][0]+=1
        for k,v in od.items():
            if v[0]==1:
                return v[1]
        return -1
        

# @lc code=end

