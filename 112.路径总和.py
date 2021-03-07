#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
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
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
 
        if not root:
            return False
        queue=deque()
        queue.append((root,root.val))

        while queue:
            node,depth =queue.popleft()
            if depth==targetSum and not node.left and not node.right:
                return True
            if node.left:
                queue.append((node.left,depth+node.left.val))
            if node.right:
                queue.append((node.right,depth+node.right.val))
                
        return False



# @lc code=end

