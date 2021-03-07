#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        small,noless=ListNode(),ListNode()
        smallhead=small
        nolesshead=noless
        while head:
            if head.val<x:
                small.next=head
                small=small.next
            else:
                noless.next=head
                noless=noless.next
            head=head.next
        noless.next=None
        small.next=nolesshead.next

        return smallhead.next

                
        
        
# @lc code=end

