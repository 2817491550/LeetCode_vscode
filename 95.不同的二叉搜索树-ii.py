#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start,end):
            if start>end:
                return [None,]
            all_trees=[]
            for i in range(start,end+1):
                left_trees=generateTrees(start,i-1)
                right_trees=generateTrees(i+1,end)
                for l in left_trees:
                    for r in right_trees:
                        currTree=TreeNode(i)
                        currTree.left=l
                        currTree.right=r
                        all_trees.append(currTree)
            return all_trees
        return generateTrees(1,n) if n else []


# @lc code=end

