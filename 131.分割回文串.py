#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str):
        
        ret=[]
        if not s:
            return ret
        n=len(s)
        def back_track(partitions,last):
            if not len(last):
                ret.append(partitions)
                return
            for i in range(len(last)):
                f_half=last[:i+1]
                r_half=last[i+1:]
                if not self.is_partition(f_half):
                    continue
                back_track(partitions+[f_half],r_half)
        back_track([],s)
        return ret
            
    def is_partition(self,substring):
            n=len(substring)
            for i in range(n//2):
                if substring[i]!=substring[n-1-i]:
                    return False
            return True

# @lc code=end

