#
# @lc app=leetcode.cn id=321 lang=python3
#
# [321] 拼接最大数
#

# @lc code=start
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def drop_loser(nums,k):
            stack=[]
            drop_counter=len(nums)-k
            for num in nums:
                while stack and stack[-1]<num and drop_counter:
                    stack.pop()
                    drop_counter-=1
                stack.append(num)
            return stack[:k]
        def merge(A,B):
            res=[]
            from collections import deque
            bigger=deque()
            A=deque(A)
            B=deque(B)
            while A or B:
                bigger=A if A>B else B
                res.append(bigger[0])
                bigger.popleft()
            return res
        return max(merge(drop_loser(nums1,i),drop_loser(nums2,k-i)) for i in range(k+1) if i<=len(nums1) and k-i <=len(nums2))

        
# @lc code=end

