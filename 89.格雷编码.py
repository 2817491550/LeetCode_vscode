#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        seen = set([0])
        def backtrack(path):
            if len(path) == 2 ** n: return path
            for i in range(n):
                nxt = 1 << i ^ path[-1]
                if nxt in seen: continue
                seen.add(nxt)
                path.append(nxt)
                if backtrack(path): return path
                path.pop()
                seen.remove(nxt)
        return backtrack([0])

# @lc code=end

