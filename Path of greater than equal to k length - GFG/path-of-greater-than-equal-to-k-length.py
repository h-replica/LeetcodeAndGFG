
class Solution:
    def pathMoreThanK (self, V, E, K, A):
        # code here
        n = V
        g = [[0 for i in range(n)]for j in range(n)]
        
        for i in range(0 , len(A) , 3) :
            g[A[i]][A[i+1]] = max(A[i+2] , g[A[i]][A[i+1]])
            g[A[i+1]][A[i]] = max(A[i+2] , g[A[i]][A[i+1]])
        visited = [0 for i in range(n)]
        def dfs(s ,  pathsum) :
            if pathsum >= K :
                return True
            
            visited[s] = 1
            
            for i in range(n) :
                if visited[i] == 1 or g[s][i] == 0 :
                    continue
                if dfs(i , pathsum+g[s][i]) :
                    visited[s] = 0
                    return True
            visited[s] = 0 
            return False
            
        return dfs(0 , 0)
            
            



#{ 
#  Driver Code Starts



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        V, E, K= map(int, input().split())
        A = list(map(int, input().split()))
        ans = ob.pathMoreThanK(V, E, K, A);
        if(ans):
            print(1)
        else:
            print(0)


# } Driver Code Ends