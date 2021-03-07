#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和，区间差分：
        # n=len(nums)
        # pre_sum=[0]*(n+1)
        # for i in range(1,n+1):
        #     pre_sum[i]=pre_sum[i-1]+nums[i-1]
        # cnt=0
        # for i in range(1,n+1):
        #     for j in range(i,n+1):
        #         if pre_sum[j]-pre_sum[i-1]==k:
        #             cnt+=1
        # ----------------------------------
        # ------------hash------------------
        sum_cnt=dict()
        sum_=0
        cnt=0
        for num in nums:
            sum_+=num
            if sum_ ==k:
                cnt+=1
            if sum_-k in sum_cnt:
                cnt+=sum_cnt[sum_-k]
            if sum_ in sum_cnt:
                sum_cnt[sum_]+=1
            else:
                sum_cnt[sum_]=1
        return cnt

       
# @lc code=end

