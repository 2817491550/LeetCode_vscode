#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic_words={"".join(sorted(s)):[] for s in strs}
        for s in strs:
            dic_words["".join(sorted(s))].append(s)
        ret=[]
        for _,v in dic_words.items():
            ret.append(v)
        return ret

# @lc code=end

