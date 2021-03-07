#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import  deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        l_to_r=True
        queue=deque()
        queue.append(root)
        ans=[]
        
        while queue:
            level_ans=deque()
            size=len(queue)
            for _ in range(size):
                node=queue.popleft()
                if l_to_r:
                    level_ans.append(node.val)
                else:
                    level_ans.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(list(level_ans))
            l_to_r=not l_to_r
        return ans
# @lc code=end

