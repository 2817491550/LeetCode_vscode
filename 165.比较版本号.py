#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=version1.split('.')
        version2=version2.split('.')
        if len(version1)>len(version2):
            version2.extend(['0']*(len(version1)-len(version2)))
        else:
            version1.extend(['0']*(len(version2)-len(version1)))
        i=j=0
        while i<len(version1) and j<len(version2):
            if int(version1[i])>int(version2[j]):
                return 1
            elif int(version1[i])<int(version2[j]):
                return -1
            else:
                i+=1
                j+=1
        if i<len(version1):
            return 1
        if j<len(version2):
            return -1
        return 0
        
# @lc code=end

