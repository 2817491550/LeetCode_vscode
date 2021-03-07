#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        pre_string=self.countAndSay(n-1)
        ret=""
        start=0
        for i in range(1,len(pre_string)):
            if pre_string[i]!=pre_string[start]:
                ret+=str(i-start)
                ret+=pre_string[start]
                start=i
        ret+=str(len(pre_string)-start)
        ret+=pre_string[start]
        return ret

        
# @lc code=end

