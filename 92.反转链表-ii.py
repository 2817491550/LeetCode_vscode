#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        if not head :
            return None
        cur,prev=head,None
        while left>1:
            prev=cur
            cur=cur.next
            left,right=left-1,right-1
        con,tail=prev,cur
        while right:
            next_node=cur.next
            cur.next=prev
            prev=cur
            cur=next_node
            right-=1
        if con:
            con.next=prev
        else:
            head=prev
        tail.next=cur
        return head



        

# @lc code=end

