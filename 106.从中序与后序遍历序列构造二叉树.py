#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(post_l,post_r,in_l,in_r):
            if post_l>post_r:
                return None
            post_root=post_r
            in_root=index[postorder[post_root]]
            post_l_sub_size=in_root-in_l
            root=TreeNode(postorder[post_root])
            root.left=helper(post_l,post_l+post_l_sub_size-1,in_l,in_root-1)
            root.right=helper(post_l+post_l_sub_size,post_r-1,in_root+1,in_r)
            return root
        n=len(postorder)
        index={inorder[i]:i for i in range(n)}
        return helper(0,n-1,0,n-1)





# @lc code=end

