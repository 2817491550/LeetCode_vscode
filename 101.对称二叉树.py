#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def helper(p,q):
            if not q and not p:
                return True
            if not q and p or not p and q:
                return False
            if q.val==p.val:
                return helper(p.left,q.right) and helper(p.right,q.left)
            else:
                return False
        return helper(root.left,root.right)
# @lc code=end

