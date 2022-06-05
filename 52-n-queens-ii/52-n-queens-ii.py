class Solution:
    def totalNQueens(self, n: int) -> int:
        positions = [[-1 , -1] for i in range(n)]
        
        
        finalAns = 0
        
        def canPlace(i , j , queen) :
            # print(positions , queen , i ,j)
            for k in range(0 ,queen ) :
                r , c = positions[k]
                if r+c == i+j or r-c == i-j or r == i or c == j :
                    return False
            return True

                
        def soln(queen , col) :
            nonlocal finalAns
            for j in range(n) :
                if canPlace(j , col , queen) :
                    if queen == n-1 :
                        finalAns+=1
                        return 
                    
                    
                    positions[queen] = [j , col]
                    soln(queen+1 , col+1)
                    positions[queen] = [-1 , -1]
                    
        soln(0 , 0)
        return finalAns