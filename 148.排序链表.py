#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sort_func(head,tail):
            if not head:
                return head
            if head.next==tail:
                head.next=None
                return head
            slow,fast=head,head
            while fast!=tail:
                slow=slow.next
                fast=fast.next
                if fast!=tail:
                    fast=fast.next
            mid=slow
            return merge(sort_func(head,mid),sort_func(mid,tail))
        def merge(a,b):
            dummyHead=ListNode()
            foot,ptr1,ptr2=dummyHead,a,b
            while ptr1 and ptr2:
                if ptr1.val<ptr2.val:
                    foot.next=ptr1
                    ptr1=ptr1.next
                else:
                    foot.next=ptr2
                    ptr2=ptr2.next
                foot=foot.next
            foot.next=ptr1 if ptr1 else ptr2
            return dummyHead.next
        return sort_func(head,None) 
# @lc code=end

