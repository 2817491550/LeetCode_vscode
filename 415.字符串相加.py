#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans=""
        count=0
        i=len(num1)-1
        j=len(num2)-1
        while i>=0 or j>=0:
            case1=num1[i] if i>=0 else '0'
            case2=num2[j] if j>=0 else '0'
            curr_result=int(case1)+int(case2)+count

            re=curr_result%10
            count=curr_result//10
            ans=str(re)+ans
            
            i-=1
            j-=1
        if count:
            ans=str(count)+ans
      

        return ans 
# @lc code=end

