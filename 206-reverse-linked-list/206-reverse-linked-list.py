# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head : return
        curr = head
        prev = None
        nextt = curr.next
            
        while(curr) :
            curr.next = prev
            prev = curr
            curr = nextt
            if nextt :
                nextt = nextt.next
        return prev