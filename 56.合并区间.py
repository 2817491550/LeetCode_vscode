#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda t:t[0])
        merged=[]
        for interval in intervals:
            if not merged or merged[-1][-1]<interval[0]:
                merged.append(interval)
            else:
                merged[-1][-1]=max(merged[-1][-1],interval[-1])
        return merged


# @lc code=end

