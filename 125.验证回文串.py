#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
def filter_string(s:str)->str:
        filtered_string=""
        for str in s:
            if str <='z' and str>='a' or str<='9'and str>='0' or str>='A' and str<='Z':
                filtered_string+=str
        return filtered_string
class Solution:
    
        
    def isPalindrome(self, s: str) -> bool:
        filtered_string=filter_string(s)
        reversed_string=filtered_string[::-1]
        return filtered_string.lower()==reversed_string.lower()

        


# @lc code=end

