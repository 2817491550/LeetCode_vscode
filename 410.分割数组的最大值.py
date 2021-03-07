#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(sum_):
            cnt=1
            total=0
            for num in nums:
                if total+num>sum_:
                    cnt+=1
                    total=num
                else:
                    total+=num
            return cnt<=m
        l=max(nums)
        r=sum(nums)
        while l<r:
            mid=l+(r-l)//2
            if check(mid):
                r=mid
            else:
                l=mid+1
        return l
# @lc code=end

