class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        dp = [0]*(n + 1)
        res = ""
        
        #Get changes
        for u, v, w in shifts:
            if w:
                dp[u] += 1
                dp[v + 1] -= 1
            else:
                dp[u] -= 1
                dp[v + 1] += 1
                    
        #Prefix sum
        for idx in range(1, n):
            dp[idx] += dp[idx - 1]
        
        #Apply changes
        for idx in range(n):
            res += chr((ord(s[idx]) - ord('a') + dp[idx]) % 26 + ord('a'))
        
        return res