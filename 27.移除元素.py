#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt=0
        i=0
        n=len(nums)
        while i<n:
            if nums[i]==val:
                del nums[i]
                n-=1
            else:
                cnt+=1
                i+=1
        return cnt
# @lc code=end

