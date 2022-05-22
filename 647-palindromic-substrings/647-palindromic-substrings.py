class Solution:
    def countSubstrings(self, s: str) -> int:
        pal = 0
        n = len(s)
        #for odd length pallinrome
        
        for k in range(n) :
            i = k
            j = k
            while(i >= 0 and  j < n) :
                if i == j :
                    pal +=1
                    i-=1
                    j+=1
                
                elif s[i] == s[j] :
                    pal+=1
                    i-=1
                    j+=1
                
                else:
                    break
                    
        for k in range(n-1) :
            i = k
            j = k+1
            while(i >= 0 and  j < n) :
                
                if s[i] == s[j] :
                    pal+=1
                    i-=1
                    j+=1
                
                else:
                    break
        return pal
        
        
            
        