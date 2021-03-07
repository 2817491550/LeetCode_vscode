#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        Ls=s.split()
        if not Ls:
            return 0
        return len(Ls[-1])
# @lc code=end

