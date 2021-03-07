#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=point=ListNode(0)
        carry=0

        while l1 or l2:
            new_point=ListNode(0)
            if not l1:
                sum_=l2.val+carry
                new_point.val=sum_%10
                carry=sum_//10
                l2=l2.next
            elif not l2:
                sum_=l1.val+carry
                new_point.val=sum_%10
                carry=sum_//10
                l1=l1.next
            else:
                sum_=(l1.val+l2.val+carry)
                new_point.val=sum_%10
                carry=sum_//10
                l1=l1.next
                l2=l2.next
            point.next=new_point
            point=point.next
        if carry:
            new_point=ListNode(1)
            point.next=new_point
        return head.next

# @lc code=end

