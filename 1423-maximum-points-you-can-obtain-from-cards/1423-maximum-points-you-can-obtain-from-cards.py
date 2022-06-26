class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        i = 0
        j = n-k-1
        totalsum = sum(cardPoints)
        s = sum(cardPoints[i:j+1])
        
        maxnow = totalsum - s
        
        while(j < n-1) :
            i+=1
            j+=1
            
            s = s - cardPoints[i-1] + cardPoints[j]
            
            maxnow = max(maxnow , totalsum - s)
        
        return maxnow
            
        