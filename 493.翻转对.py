#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums,0,len(nums)-1)
    def mergeSort(self,nums,start,end):
        if start>=end:
            return 0
        mid=(start+end)>>1
        cnt=self.mergeSort(nums,start,mid)+self.mergeSort(nums,mid+1,end)
        cache=[]
        i=start
        t=start
        for j in range(mid+1,end+1):
            while i<=mid and nums[i]<=2*nums[j]:i+=1
            while t<=mid and nums[t]<nums[j] :
                cache.append(nums[t])
                t+=1
            cache.append(nums[j])
            cnt+=mid-i+1
        while t<=mid:
            cache.append(nums[t])
            t+=1
        nums[start:end+1]=cache
        return cnt        
        
# @lc code=end

