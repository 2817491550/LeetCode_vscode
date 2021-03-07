#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        is_Sorted=[-float('inf')]
        def inorder(root):
            if root:
                inorder(root.left)
                is_Sorted.append(root.val)
                inorder(root.right)
            
        inorder(root)

        for i in range(1,len(is_Sorted)):
            if is_Sorted[i]<=is_Sorted[i-1]:
                return False
        return True



        


# @lc code=end

