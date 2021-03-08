#
# @lc app=leetcode.cn id=871 lang=python3
#
# [871] 最低加油次数
#

# @lc code=start
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        n=len(stations)
        dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=startFuel
        for i in range(1,n+1):
            for j in range(1,i+1):
                if dp[i-1][j]>=stations[i-1][0]:
                    dp[i][j]=dp[i-1][j]
                if dp[i-1][j-1]>=stations[i-1][0]:
                    dp[i][j]=max(dp[i-1][j-1]+stations[i-1][1],dp[i][j])
        
        for j in range(n+1):
            if dp[n][j]>=target:
                return j
        return -1
        # 可以进行空间压缩+状态压缩
                
        
# @lc code=end

