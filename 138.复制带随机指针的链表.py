#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.node_hash=dict()
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        if head in self.node_hash:
            return self.node_hash[head]
        node=Node(head.val)
        self.node_hash[head]=node
        node.next=self.copyRandomList(head.next)
        node.random=self.copyRandomList(head.random)
        return node
# @lc code=end

