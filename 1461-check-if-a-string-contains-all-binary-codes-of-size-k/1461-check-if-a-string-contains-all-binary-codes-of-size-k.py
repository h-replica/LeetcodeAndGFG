class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        total = 1 << k
        start = s[0:k]
        bcode = set()
        bcode.add(start)
        
        i = k
        while(i < len(s)):
            start = start[1:] + s[i]
            bcode.add(start)
            i+=1
            if len(bcode) == total :
                return True
        return False
            
#         """
#             Rolling hash algo
            
#         """
        
#         bcode = set()
#         total = 1 << k 
#         allones = total-1
#         start = 0
        
#         for i in range(len(s)) :
#             start = ((start << 1 )& allones)| int(s[i])
#             bcode.add(start)
#             if(i >= k and len(bcode) == total) :return True
#         return False
    
            
            