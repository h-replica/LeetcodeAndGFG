class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n , m = len(matrix) , len(matrix[0])
        
        visited = [[0 for i in range(m)]for j in range(n)]
        maxm = 1

        dp = [[0 for i in range(m)]for j in range(n)]
        
        
        def dfs(i , j) :
            if dp[i][j] :
                return dp[i][j]
            visited[i][j] = 1
            dr = [0 ,0 , 1 , -1]
            dc = [1 , -1 , 0 , 0]
            
            maxmfromij = 0
            for k in range(4) :
                rr = i + dr[k]
                cc = j + dc[k]
                
                if rr < 0 or cc < 0 or rr >= n or cc >= m or visited[rr][cc] == 1 or matrix[rr][cc] <= matrix[i][j] :
                    continue
                
                maxmfromij = max(maxmfromij , dfs(rr , cc))
            
            visited[i][j] = 0
            dp[i][j] = maxmfromij+1
            return maxmfromij +1
        
        for i in range(n) :
            for j in range(m) :
                if visited[i][j] == 0 :
                    now = dfs(i,j)
                    maxm = max(now , maxm)
        return maxm