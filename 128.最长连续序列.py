#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet=set(nums)
        lgst_seq_len=0
        for num in nums:
            if num-1 not in numsSet:
                current_num=num
                current_len=1
                while current_num+1 in numsSet:
                    current_num=current_num+1
                    current_len+=1
                lgst_seq_len=max(lgst_seq_len,current_len)

        return lgst_seq_len


# @lc code=end

