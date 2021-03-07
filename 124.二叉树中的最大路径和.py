#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def max_score(node):
            if not node:
                return 0
            left_score=max(0,max_score(node.left))
            right_score=max(0,max_score(node.right))
            path_score=node.val+left_score+right_score
            self.max_sum=max(self.max_sum,path_score)
            return node.val+max(left_score,right_score)
        self.max_sum=-float('inf')
        max_score(root)
        return self.max_sum
    
# @lc code=end

