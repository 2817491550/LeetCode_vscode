#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n=len(s)
        wordDict=set(wordDict)
        import functools
        @functools.lru_cache(None)
        def back_track(index):
            # terminator
            if index==n:
                return [[]]
            ans=[]
            for i in range(index+1,n+1):
                word=s[index:i]
                if word in wordDict:
                    nextWordBreaks=back_track(i)
                    for nextWordBreak in nextWordBreaks:
                        ans.append(nextWordBreak.copy()+[word])
            return ans
        breakList=back_track(0)
        return [" ".join(words[::-1]) for words in breakList]


# @lc code=end

