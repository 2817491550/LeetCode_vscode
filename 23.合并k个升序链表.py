#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge_(l,r):
            if l==r:
                return lists[l]
            if l>r:
                return None
            mid=l+(r-l)//2
            return self.mergeTwoLists(merge_(l,mid),merge_(mid+1,r))
        n=len(lists)
        return merge_(0,n-1)
    def mergeTwoLists(self,l1,l2):
        if not l1 or not l2:
            return l1 if l1 else l2
        head=ListNode()
        foot=head
        ptr1=l1 
        ptr2=l2
        while ptr2 and ptr1:
            if ptr1.val<ptr2.val:
                foot.next=ptr1
                ptr1=ptr1.next
            else:
                foot.next=ptr2
                ptr2=ptr2.next
            foot=foot.next
        foot.next=ptr1 if ptr1 else ptr2 
        return head.next
        

# @lc code=end

