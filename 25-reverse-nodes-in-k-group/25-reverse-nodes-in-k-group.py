# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def length(curr) :
            size = 0
            while(curr):
                size+=1
                curr= curr.next
            return size
            
        def reverse(head) :
            l = length(head)
            if l <= 1 :
                return head
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
        
        n = length(head)
        
        part = n//k
        
        if part == 0 :
            return head
        
        heads = []
        print(part)
        for i in range(part) :
            curr = head 
            j = 1 
            while(j < k) :
                curr = curr.next
                j+=1
            
            heads.append(head)
            head = curr.next
            curr.next = None
        
        reversehead = []
        
        for headpart in heads :
            reversehead.append(reverse(headpart))
        
        curr = reversehead[0]
        while(curr.next) :
            curr = curr.next
        for i in range(1 ,part) :
            headpart = reversehead[i]
            curr.next = headpart
            curr = headpart
            while(curr.next) :
                curr = curr.next
        
        if n%k != 0 :
            curr.next = head
        
        return reversehead[0]
            
        
        
        
                
                
        
                
            