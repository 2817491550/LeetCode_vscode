#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        n=len(nums)
        self.Range_sums=[0]*(n+1)
        for i,num in enumerate(nums):
            if i>0:
                self.Range_sums[i+1]=self.Range_sums[i]+num
            else:
                self.Range_sums[i+1]=nums[i]
        



    def sumRange(self, i: int, j: int) -> int:
        return self.Range_sums[j+1]-self.Range_sums[i]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

