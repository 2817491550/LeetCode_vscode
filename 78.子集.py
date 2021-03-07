#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        # for num in nums:
        #     newsets=[]
        #     for subset in ans:
        #         new_subset=subset+[num]
        #         newsets.append(new_subset)
        #     print(newsets)
        #     ans.extend(newsets)
        def backtrack(length,index,subset):
            if length==len(subset):
                ans.append(subset)
                return
            for i in range(index,len(nums)):
                backtrack(length,i+1,subset+[nums[i]])
                
        for i in range(1,len(nums)+1):
            backtrack(i,0,[])
        return ans



# @lc code=end

