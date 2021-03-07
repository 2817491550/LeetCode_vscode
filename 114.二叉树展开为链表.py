#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preordList=[]
        def preorder(root):
            if root:
                preordList.append(root)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        for i in range(1,len(preordList)):
            pre,cur=preordList[i-1],preordList[i]
            pre.left=None
            pre.right=cur
        



# @lc code=end

