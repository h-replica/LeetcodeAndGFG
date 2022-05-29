class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort(key = lambda x : -len(x))
        bitset = []
        
        for word in words :
            n = 0
            for j in word :
                n = (1 << (ord(j) - ord("a"))) | n
            bitset.append(n)

        maxans = 0
        for i in range(0 ,len(words)) :
            for j in range(i+1 , len(words)) :
                
                if (bitset[i] & bitset[j]) != 0 :
                    
                    continue
                
                maxans = max(maxans , len(words[i])*len(words[j]))
                
                break
        return maxans
            
                