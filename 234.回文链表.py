#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        # arr=[]
        # while head is not None:
        #     arr.append(head.val)
        #     head=head.next
        # l,r=0,len(arr)-1
        # while l<r:
        #     if arr[l]!=arr[r]:
        #         return False
        #     l+=1
        #     r-=1
        # return True
        # 快慢指针
        slow,fast=head,head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        if fast is not None:
            slow=slow.next
        fast=head
        reversedList=self.reverseList(slow)
        while reversedList is not None:
            if fast.val!=reversedList.val:
                return False
            fast=fast.next
            reversedList=reversedList.next
        return True
    def reverseList(self,head):
        current=head
        previous=None
        while current is not None:
            next_node=current.next
            current.next=previous
            previous=current
            current=next_node
        return previous
# @lc code=end

