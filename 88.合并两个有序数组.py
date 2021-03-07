#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        if m==0:
            nums1[:]=nums2[:]
            return 
        i=n-1
        j=m-1
        k=m+n-1
        while i>=0 and j>=0:
            if nums2[i]>nums1[j]:
                nums1[k]=nums2[i]
                i-=1
                k-=1
            else:
                nums1[k]=nums1[j]
                j-=1
                k-=1

        nums1[:i+1]=nums2[:i+1]
        


# @lc code=end

