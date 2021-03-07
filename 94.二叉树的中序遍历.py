#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(root,r):
        if root:
            inorder(root.left,r)
            r.append(root.val)
            inorder(root.right,r)
class Solution:

    

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        inorder(root,result)
        return result
# @lc code=end

