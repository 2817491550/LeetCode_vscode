#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'
        m=len(num1)
        n=len(num2)
        ans_array=[0]*(m+n)
        for i in range(m-1,-1,-1):
            x=int(num1[i])
            for j in range(n-1,-1,-1):
                y=int(num2[j])
                ans_array[i+j+1]+=x*y
        for i in range(m+n-1,0,-1):
            ans_array[i-1]+=ans_array[i]//10
            ans_array[i]%=10
        start_index=0 if ans_array[0]!=0 else 1
        return "".join(str(x) for x in ans_array[start_index:])

# @lc code=end

