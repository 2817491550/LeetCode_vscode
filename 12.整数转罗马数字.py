#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        thousands=["","M","MM","MMM"]
        hundreds=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        tens=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        ones=["","I","II","III","IV","V","VI","VII","VIII","IX"]
        return thousands[num//1000]+hundreds[num%1000//100]+tens[num%100//10]+ones[num%10]
# @lc code=end

