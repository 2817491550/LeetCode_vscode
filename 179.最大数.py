#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class LargeNumKey(str):
    def __lt__(self,other):
        return self+other>other+self
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        LargeNum="".join(sorted(map(str,nums),key=LargeNumKey))
        return '0' if LargeNum[0]=='0' else LargeNum

# @lc code=end

