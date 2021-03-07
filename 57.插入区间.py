#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals)
        
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

