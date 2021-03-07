#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ret=[]
        if not root:
            return []
        def dfs(node,targetSum,path):
  
            if not node.left and not  node.right and targetSum==0:
                ret.append(path)
                return 
            
            if node.left:
                dfs(node.left,targetSum-node.left.val,path+[node.left.val])
            if node.right:
                dfs(node.right,targetSum-node.right.val,path+[node.right.val])
        dfs(root,targetSum-root.val,[root.val])
        return ret



# @lc code=end

