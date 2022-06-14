class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        @cache
        def lcs(a , b , i , j) :
            if i >= n or j >= m :
                return 0
            
            if a[i] == b[j] :
                return lcs(a , b , i+1 , j+1) + 1
            return max(lcs(a, b , i+1 , j) , lcs(a , b , i , j+1))
        
        same = lcs(word1 , word2 , 0 , 0)
        print(same)
        return n-same + m-same
            
            
        