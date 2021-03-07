#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummyNode=ListNode(0)
        dummyNode.next=head
        temp=dummyNode
        while temp.next:
            if head.next and head.val==head.next.val:
                while head.next and head.val==head.next.val:
                    head.next=head.next.next
                # temp.next=temp.next.next
                # head=temp.next
            else:
                temp=head
                head=head.next
        return dummyNode.next
# @lc code=end

