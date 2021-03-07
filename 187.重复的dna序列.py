#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l,n=10,len(s)
        seen,ans=set(),set()
        for start_point in range(n-l+1):
            s_in_window=s[start_point:start_point+l]
            if s_in_window in seen:
                ans.add(s_in_window)
            else:
                seen.add(s_in_window)
        return list(ans)
# @lc code=end

