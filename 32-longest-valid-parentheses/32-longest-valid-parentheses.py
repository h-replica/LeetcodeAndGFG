class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = []
        overallmax = 0
        currmax = 0
        for i in range(len(s)) :
            x = s[i]
            
            if len(st) == 0 and x == ")" :
                overallmax = max(currmax , overallmax)
                currmax = 0 
                continue
            
            if x == "(" :
                st.append(i)
            else:
                currmax+=2
                st.pop()
        
        if len(st) == 0 :
            return max(overallmax , currmax)
        
        i = len(s)-1
        probable = []
        for j in st[::-1] :
            if j == i :
                i = j-1
                continue
            probable.append(i-j)
            currmax = currmax - (i-j)
            i = j-1
            if i < 0 :
                break
        probable.append(overallmax)
        probable.append(currmax)
        return max(probable)
            
                
            
            