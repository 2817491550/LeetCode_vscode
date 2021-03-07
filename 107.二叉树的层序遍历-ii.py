#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result=deque()
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
            result.appendleft(level)
            queue=nodes
        return list(result)
# @lc code=end

