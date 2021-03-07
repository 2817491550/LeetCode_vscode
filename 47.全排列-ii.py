#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ret=[]
        used=set()
        num_used=set()
        def back_track(now,current):
            
            if now==n:
                ret.append(current)
            for i in range(n):
                if i in used:
                    continue
                if i>0 and nums[i]==nums[i-1] and i-1 in used:
                    continue
                used.add(i)
                back_track(now+1,current+[nums[i]])
                used.remove(i)
        nums.sort()
        back_track(0,[])
        return ret
# @lc code=end

