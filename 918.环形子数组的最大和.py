#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        l = len(A)
        A = A + A
        ans = A[0]
        s = [0] * (2 * l)
        q = [0]
        for i in range(1, 2 * l):
            s[i] = s[i - 1] + A[i - 1]
            while q and q[0] < i - l:
                q.pop(0)
            ans = max(ans, s[i] - s[q[0]])
            while q and s[q[-1]] > s[i]:
                q.pop()
            q.append(i)
        return ans

# @lc code=end

