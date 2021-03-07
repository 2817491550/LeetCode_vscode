#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack_num1=[]
        stack_num2=[]
        while l1:
            stack_num1.append(l1.val)
            l1=l1.next
        while l2:
            stack_num2.append(l2.val)
            l2=l2.next
        ans=ListNode(0)
        carry=0
        while stack_num1 or stack_num2 or carry:
            val=carry
            val+=stack_num1.pop() if stack_num1 else 0
            val+=stack_num2.pop() if stack_num2 else 0
            carry,val=divmod(val,10)
            temp=ListNode(val)
            temp.next=ans.next
            ans.next=temp

        return ans.next



        
# @lc code=end

