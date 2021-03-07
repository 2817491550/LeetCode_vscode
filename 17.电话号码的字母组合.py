#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        ans=[]
        letters_dict={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        def search(string,digits,index,result):
            if index==len(digits):
                result.append(string)
                return 
            letters=letters_dict[digits[index]]
            for letter in letters:
                search(string+letter,digits,index+1,result)
        search("",digits,0,ans)
        return ans





# @lc code=end

