#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==0 or num==1:
            return True
        left=1
        right=num
        while left<=right:
            mid=int(left+(right-left)/2)
            # print("left:{}_mid:{}_right:{}".format(left,mid,right))
            if mid*mid==num:
                return True
            elif mid*mid>num:
                right=mid-1
            else:
                left=mid+1
        return False

# @lc code=end

