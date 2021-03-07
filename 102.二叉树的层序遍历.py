#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result=[]
        queue=[root]
        while queue:
            nodes=[]
            level=[]
            for item in queue:
                level.append(item.val)
                if item.left:
                    nodes.append(item.left)
                if item.right:
                    nodes.append(item.right)
            result.append(level)
            queue=nodes
        return result
        
            
# @lc code=end

