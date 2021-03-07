#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        nums.sort()
        # for num in nums:
        #     newsets=[]
        #     for subset in ans:
        #         new_subset=subset+[num]
        #         if not new_subset in ans:
        #             newsets.append(new_subset)
        #     # print(newsets)
        #     ans.extend(newsets)
        def backtrack(length,index,subset):
            if length==len(subset) and subset not in ans:
                ans.append(subset)
                return
            for i in range(index,len(nums)):
                backtrack(length,i+1,subset+[nums[i]])
                
        for i in range(1,len(nums)+1):
            backtrack(i,0,[])
        return ans


# @lc code=end

