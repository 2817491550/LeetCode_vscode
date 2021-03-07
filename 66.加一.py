#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=0
        all_nine=True
        for i in digits:
            if i!=9:
                all_nine=False
        if all_nine:
            return [1]+[0]*len(digits)        
        n=len(digits)
        def add_one(reverse_index):
            if digits[reverse_index]!=9:
                digits[reverse_index]+=1
            else:
                digits[reverse_index]=0
                add_one(reverse_index-1)
        add_one(n-1)
        return digits


            



# @lc code=end

