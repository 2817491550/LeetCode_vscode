#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return "{0:b}".format(int(a,2)+int(b,2))
        ans=[]
        n=max(len(a),len(b))
        carry=0
        for i in range(n):
            carry+=int(a[len(a)-1-i]) if i<len(a) else 0
            carry+=int(b[len(b)-1-i]) if i<len(b) else 0
            ans.append(str(carry%2))
            # print(str(carry%2))
            carry//=2
        if carry>0:
            ans.append('1')
        # ans=ans.reverse()
        return "".join(ans[::-1])

# @lc code=end

