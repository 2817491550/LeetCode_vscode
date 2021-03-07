#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes=[]
        def inorder(root):
            if root:
                inorder(root.left)
                nodes.append(root)
                inorder(root.right)
        inorder(root)
        x,y=None,None
        pre=nodes[0]
        for i in  range(1,len(nodes)):
            if pre.val>nodes[i].val:
                x=nodes[i]
                if not y:
                    y=pre
            pre=nodes[i]
        if x and y:
            x.val,y.val=y.val,x.val
            
# @lc code=end

