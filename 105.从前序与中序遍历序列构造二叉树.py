#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(pre_l,pre_r,in_l,in_r):
            if pre_l>pre_r:
                return None
            pre_root=pre_l
            in_root=index[preorder[pre_root]]
            pre_l_sub_size=in_root-in_l
            root=TreeNode(preorder[pre_root])
            root.left=helper(pre_l+1,pre_l+pre_l_sub_size,in_l,in_root-1)
            root.right=helper(pre_l+pre_l_sub_size+1,pre_r,in_root+1,in_r)
            return root
        n=len(preorder)
        index={inorder[i]:i for i in range(n)}
        return helper(0,n-1,0,n-1)





# @lc code=end

