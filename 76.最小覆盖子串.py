#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter=Counter(t)
        win_counter=dict()
        distance=0
        left,right=0,0
        n=len(s)
        min_len=len(s)+1
        begin=0
        tlen=len(t)
        while right<n:
            if distance<tlen:
                win_counter[]

# @lc code=end

