# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        size = 0
        curr = head 
        while(curr):
            size+=1
            curr= curr.next
        
        if size <= 1 :
            return head
        
        left = min(k , size-k+1)
        right = max(k , size-k+1)
        
        prev1 = None
        curr1 = head
        next1 = curr1.next
        
        
        i = left
        while(i > 1) :
            prev1 = curr1 
            curr1 = next1
            next1 = next1.next
            i-=1
            
        
        prev2 = None
        curr2 = head
        next2  =curr2.next
        
        i = right
        while(i > 1) :
            prev2 = curr2 
            curr2 = next2
            next2 = next2.next
            i-=1
        
        
        
        
        if prev1 : prev1.next = curr2 #prev1 can be none
        
        if prev2 == curr1 :  #if we need to swap adjascent nodes , prev2 will never be none for linked list havinf size greater than 1
            curr2.next = curr1
            curr1.next = next2
        else:    
            prev2.next = curr1
            curr1.next = next2
            curr2.next = next1
        
        return curr2 if not prev1 else head  #when the head gets changed itself , curr1 = head , then curr2 will become new head 
        return head
        
            
            