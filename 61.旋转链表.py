#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        length=1
        tail=head
        while tail.next:
            length+=1
            tail=tail.next
        k=k%length
        tail.next=head
        for _ in range(length-k):
            tail=tail.next
        head=tail.next
        tail.next=None
        return head
# @lc code=end

