#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1+=nums2
        nums1.sort()
        if len(nums1)%2==0:
            return (nums1[int(len(nums1)/2)]+nums1[int(len(nums1)/2-1)])/2

        else:
            return float(nums1[int(len(nums1)//2)])
# @lc code=end

