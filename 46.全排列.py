#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ret=[]
        used=set()
        def back_track(now,current):
            
            if now==n:
                ret.append(current)
            for i in nums:
                if i not in used:
                    used.add(i)
                    back_track(now+1,current+[i])
                    used.remove(i)
        back_track(0,[])
        return ret
# @lc code=end