class Solution:
    def largestPalindromic(self, num: str) -> str:
        f = ""
        b = ""
        single = "0"
        flag = 0
        
        
        haveeven = 0
        ls = sorted(num , reverse = True)
        n = len(num)
        i=0
        while(i < n) :
            if i == n-1 :
                flag = 1
                single = max(single , ls[i] )
                break
                
            if ls[i] == "0" and haveeven == 0:
                i+=1
                continue
            
            if ls[i] == ls[i+1] :
                f += ls[i]
                b = ls[i+1] +b
                haveeven = 1
                i+=2
            else:
                flag = 1
                single = max(single , ls[i])
                i+=1
                
                
        if flag == 1 :
            return f+single+b
        return f+b
                
            